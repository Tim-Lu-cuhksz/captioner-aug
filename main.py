import logging
from typing import Dict, List, Tuple

import click
import pandas as pd
from omegaconf import OmegaConf
from tqdm import tqdm

import wandb
from components.evaluator import GPTEvaluator, NullEvaluator
from components.proposer import (
    LLMProposer,
    LLMProposerDiffusion,
    VLMFeatureProposer,
    VLMProposer,
)
from components.ranker import CLIPRanker, LLMRanker, NullRanker, VLMRanker


def load_config(config: str) -> Dict:
    base_cfg = OmegaConf.load("configs/base.yaml")
    cfg = OmegaConf.load(config)
    final_cfg = OmegaConf.merge(base_cfg, cfg)
    args = OmegaConf.to_container(final_cfg)
    args["config"] = config
    if args["wandb"]:
        wandb.init(
            project=args["project"],
            name=args["data"]["name"],
            group=f'{args["data"]["group1"]} - {args["data"]["group2"]} ({args["data"]["purity"]})',
            config=args,
        )
    return args


def load_data(args: Dict) -> Tuple[List[Dict], List[Dict], List[str]]:
    data_args = args["data"]

    df = pd.read_csv(f"{data_args['root']}/{data_args['name']}.csv")

    if data_args["subset"]:
        old_len = len(df)
        df = df[df["subset"] == data_args["subset"]]
        print(
            f"Taking {data_args['subset']} subset (dataset size reduced from {old_len} to {len(df)})"
        )

    dataset1 = df[df["group_name"] == data_args["group1"]].to_dict("records")
    dataset2 = df[df["group_name"] == data_args["group2"]].to_dict("records")
    group_names = [data_args["group1"], data_args["group2"]]

    if data_args["purity"] < 1:
        logging.warning(f"Purity is set to {data_args['purity']}. Swapping groups.")
        assert len(dataset1) == len(dataset2), "Groups must be of equal size"
        n_swap = int((1 - data_args["purity"]) * len(dataset1))
        dataset1 = dataset1[n_swap:] + dataset2[:n_swap]
        dataset2 = dataset2[n_swap:] + dataset1[:n_swap]
    return dataset1, dataset2, group_names


def propose(args: Dict, dataset1: List[Dict], dataset2: List[Dict]) -> List[str]:
    proposer_args = args["proposer"]
    proposer_args["seed"] = args["seed"]
    proposer_args["captioner"] = args["captioner"]

    proposer = eval(proposer_args["method"])(proposer_args)
    hypotheses, logs, images = proposer.propose(dataset1, dataset2)
    if args["wandb"]:
        wandb.log({"logs": wandb.Table(dataframe=pd.DataFrame(logs))})
        for i in range(len(images)):
            wandb.log(
                {
                    f"group 1 images ({dataset1[0]['group_name']})": images[i][
                        "images_group_1"
                    ],
                    f"group 2 images ({dataset2[0]['group_name']})": images[i][
                        "images_group_2"
                    ],
                }
            )
    return hypotheses


def rank(
    args: Dict,
    hypotheses: List[str],
    dataset1: List[Dict],
    dataset2: List[Dict],
    group_names: List[str],
) -> List[str]:
    ranker_args = args["ranker"]
    ranker_args["seed"] = args["seed"]

    ranker = eval(ranker_args["method"])(ranker_args)

    scored_hypotheses = ranker.rerank_hypotheses(hypotheses, dataset1, dataset2)
    if args["wandb"]:
        table_hypotheses = wandb.Table(dataframe=pd.DataFrame(scored_hypotheses))
        wandb.log({"scored hypotheses": table_hypotheses})
        for i in range(5):
            wandb.summary[f"top_{i + 1}_difference"] = scored_hypotheses[i][
                "hypothesis"
            ].replace('"', "")
            wandb.summary[f"top_{i + 1}_score"] = scored_hypotheses[i]["auroc"]

    scored_groundtruth = ranker.rerank_hypotheses(
        group_names,
        dataset1,
        dataset2,
    )
    if args["wandb"]:
        table_groundtruth = wandb.Table(dataframe=pd.DataFrame(scored_groundtruth))
        wandb.log({"scored groundtruth": table_groundtruth})

    return [hypothesis["hypothesis"] for hypothesis in scored_hypotheses]


def evaluate(args: Dict, ranked_hypotheses: List[str], group_names: List[str]) -> Dict:
    evaluator_args = args["evaluator"]

    evaluator = eval(evaluator_args["method"])(evaluator_args)

    metrics, evaluated_hypotheses = evaluator.evaluate(
        ranked_hypotheses,
        group_names[0],
        group_names[1],
    )

    if args["wandb"] and evaluator_args["method"] != "NullEvaluator":
        table_evaluated_hypotheses = wandb.Table(
            dataframe=pd.DataFrame(evaluated_hypotheses)
        )
        wandb.log({"evaluated hypotheses": table_evaluated_hypotheses})
        wandb.log(metrics)
    return metrics

# @click.command()
# @click.option("--config", help="config file")
def main(config, external_hypo=None):
    logging.info("Loading config...")
    args = load_config(config)
    # print(args)

    logging.info("Loading data...")
    dataset1, dataset2, group_names = load_data(args)
    print(dataset1, dataset2, group_names)

    logging.info("Proposing hypotheses...")
    if not external_hypo:
        hypotheses = propose(args, dataset1, dataset2)
    else:
        hypotheses = external_hypo
    print(hypotheses)

    logging.info("Ranking hypotheses...")
    ranked_hypotheses = rank(args, hypotheses, dataset1, dataset2, group_names)
    print(ranked_hypotheses)

    logging.info("Evaluating hypotheses...")
    metrics = evaluate(args, ranked_hypotheses, group_names)
    print(metrics)
    return metrics

def PIS_eval(n_classes = 21, difficulty_level = 0):
    from data.generate_csv_PIS import write_to_csv_and_yaml, write_to_csv_and_yaml_blur, write_to_csv_and_yaml_gaussian
    from data.generate_csv_PIS import write_to_csv_and_yaml_sp, write_to_csv_and_yaml_brighten
    acc1 = []
    acc5 = []

    # n_samples = 21
    assert difficulty_level in [0, 1, 2]
    for i in tqdm(range(n_classes)):
        config_file = write_to_csv_and_yaml(difficulty_idx=difficulty_level, class_idx=i)
        # config_file = write_to_csv_and_yaml_blur(difficulty_idx=difficulty_level, class_idx=i)
        # config_file = write_to_csv_and_yaml_gaussian(difficulty_idx=difficulty_level, class_idx=i)
        # config_file = write_to_csv_and_yaml_sp(difficulty_idx=difficulty_level, class_idx=i)
        # config_file = write_to_csv_and_yaml_brighten(difficulty_idx=difficulty_level, class_idx=i)
        print(config_file)
        metrics = main(config_file)
        acc1.append(metrics['acc@1'])
        acc5.append(metrics['acc@5'])

    print()
    print('Number of pairs: ', len(acc1))
    print(f'acc@1: {sum(acc1) / len(acc1):.2f}')
    print(f'acc@5: {sum(acc5) / len(acc5):.2f}')

def imagenet_eval(n_classes = 7, task = 'styles'):
    from data.generate_csv_imagenet import write_to_csv_and_yaml, write_to_csv_and_yaml_blur, write_to_csv_and_yaml_gaussian
    from data.generate_csv_imagenet import write_to_csv_and_yaml_sp, write_to_csv_and_yaml_brighten
    acc1 = []
    acc5 = []

    for i in range(n_classes):
        for j in range(i + 1, n_classes):
            config_file = write_to_csv_and_yaml(class_idx1=i, class_idx2=j, task=task)
            # config_file = write_to_csv_and_yaml_blur(class_idx1=i, class_idx2=j, task=task)
            # config_file = write_to_csv_and_yaml_gaussian(class_idx1=i, class_idx2=j, task=task)
            # config_file = write_to_csv_and_yaml_sp(class_idx1=i, class_idx2=j, task=task)
            # config_file = write_to_csv_and_yaml_brighten(class_idx1=i, class_idx2=j, task=task)
            print(config_file)
            metrics = main(config_file)
            acc1.append(metrics['acc@1'])
            acc5.append(metrics['acc@5'])
    print()
    print('Number of pairs: ', len(acc1))
    print(f'acc@1: {sum(acc1) / len(acc1):.2f}')
    print(f'acc@5: {sum(acc5) / len(acc5):.2f}')

if __name__ == "__main__":
    # from data.generate_csv_PIS import write_to_csv_and_yaml
    # class_idx = 0,1,...,20
    # difficulty_idx= 0 (easy), 1 (medium), 2 (hard)
    # config_file = write_to_csv_and_yaml(difficulty_idx=2, class_idx=20) 
    # print(config_file)
    # metrics = main(config_file)
    PIS_eval(n_classes=7, difficulty_level=0)

    # from data.generate_csv_imagenet import write_to_csv_and_yaml, write_to_csv_and_yaml_blur
    # # i = 0,1,...,6; j = i+1,...,6
    # task = 'styles' #, 'classes'
    # config_file = write_to_csv_and_yaml_blur(class_idx1=0, class_idx2=1, task=task)
    # print(config_file)
    # metrics = main(config_file)
    # imagenet_eval(n_classes=5, task='classes')

