import csv
import json
import yaml

difficulty = ['easy', 'medium', 'hard']

def write_to_csv_and_yaml(
        difficulty_idx = 0,
        class_idx = 0,
        num_images_per_set = 10

):
    base_path = f'./data/pairedimagesets/VisDiff/{difficulty[difficulty_idx]}'
    jsonl_path = f'./data/pairedimagesets/VisDiff/{difficulty[difficulty_idx]}.jsonl'
    output_csv = f'./data/PIS_{difficulty[difficulty_idx]}'
    output_yaml = f'./configs/PIS_{difficulty[difficulty_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set2']}", "path": path})
    
    # Write the rows to a CSV file
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")

    data = {
        'data': {
            'name': f"PIS_{difficulty[difficulty_idx]}",
            'group1': lines[class_idx]['set1'],
            'group2': lines[class_idx]['set2']
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_blur(
        difficulty_idx = 0,
        class_idx = 0,
        num_images_per_set = 10

):
    base_path = f'./data/pairedimagesets/VisDiff-blurred/{difficulty[difficulty_idx]}'
    jsonl_path = f'./data/pairedimagesets/VisDiff-blurred/{difficulty[difficulty_idx]}.jsonl'
    output_csv = f'./data/PIS_{difficulty[difficulty_idx]}'
    output_yaml = f'./configs/PIS_{difficulty[difficulty_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}" + " with blurry effect", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set2']}" + " with blurry effect", "path": path})
    
    # Write the rows to a CSV file
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")

    data = {
        'data': {
            'name': f"PIS_{difficulty[difficulty_idx]}",
            'group1': lines[class_idx]['set1'] + " with blurry effect",
            'group2': lines[class_idx]['set2'] + " with blurry effect"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_gaussian(
        difficulty_idx = 0,
        class_idx = 0,
        num_images_per_set = 10

):
    base_path = f'./data/pairedimagesets/VisDiff-gaussian/{difficulty[difficulty_idx]}'
    jsonl_path = f'./data/pairedimagesets/VisDiff-gaussian/{difficulty[difficulty_idx]}.jsonl'
    output_csv = f'./data/PIS_{difficulty[difficulty_idx]}'
    output_yaml = f'./configs/PIS_{difficulty[difficulty_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}" + " with Gaussian noise", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set2']}" + " with Gaussian noise", "path": path})
    
    # Write the rows to a CSV file
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")

    data = {
        'data': {
            'name': f"PIS_{difficulty[difficulty_idx]}",
            'group1': lines[class_idx]['set1'] + " with Gaussian noise",
            'group2': lines[class_idx]['set2'] + " with Gaussian noise"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_sp(
        difficulty_idx = 0,
        class_idx = 0,
        num_images_per_set = 10

):
    base_path = f'./data/pairedimagesets/VisDiff-sp/{difficulty[difficulty_idx]}'
    jsonl_path = f'./data/pairedimagesets/VisDiff-sp/{difficulty[difficulty_idx]}.jsonl'
    output_csv = f'./data/PIS_{difficulty[difficulty_idx]}'
    output_yaml = f'./configs/PIS_{difficulty[difficulty_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}" + " with salt and pepper noise", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2/{i}.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set2']}" + " with salt and pepper noise", "path": path})
    
    # Write the rows to a CSV file
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")

    data = {
        'data': {
            'name': f"PIS_{difficulty[difficulty_idx]}",
            'group1': lines[class_idx]['set1'] + " with salt and pepper noise",
            'group2': lines[class_idx]['set2'] + " with salt and pepper noise"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'


def write_to_csv_and_yaml_brighten(
        difficulty_idx = 0,
        class_idx = 0,
        num_images_per_set = 10

):
    base_path = f'./data/pairedimagesets/VisDiff-brightened/{difficulty[difficulty_idx]}'
    jsonl_path = f'./data/pairedimagesets/VisDiff-brightened/{difficulty[difficulty_idx]}.jsonl'
    output_csv = f'./data/PIS_{difficulty[difficulty_idx]}'
    output_yaml = f'./configs/PIS_{difficulty[difficulty_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1/{i}_brightened.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}" + " with high brightness", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2/{i}_brightened.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set2']}" + " with high brightness", "path": path})
    
    # Write the rows to a CSV file
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")

    data = {
        'data': {
            'name': f"PIS_{difficulty[difficulty_idx]}",
            'group1': lines[class_idx]['set1'] + " with high brightness",
            'group2': lines[class_idx]['set2'] + " with high brightness"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'