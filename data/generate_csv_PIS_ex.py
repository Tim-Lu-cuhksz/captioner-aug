import csv
import json
import yaml

shifts = ["co_occurrence_shift", "context_shift", "cultural_shift", "emotional_shift", "seasonal_shift", "viewpoint_shift"]

def write_to_csv_and_yaml(
        shift_idx = 0,
        class_idx = 0,
        num_images_per_set = 1

):
    base_path = f'./data/PIS_extension/{shifts[shift_idx]}'
    jsonl_path = f'./data/PIS_extension/{shifts[shift_idx]}.jsonl'
    output_csv = f'./data/PIS_{shifts[shift_idx]}'
    output_yaml = f'./configs/PIS_{shifts[shift_idx]}'

    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    
    rows = []
    # For class 1
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_1.jpg'
        rows.append({"group_name": f"{lines[class_idx]['set1']}", "path": path})
    
    # # For class2 images: assuming a similar naming pattern: ./data/class2/class2_0.jpg, ..., ./data/class2/class2_9.jpg
    for i in range(num_images_per_set):
        path = f'{base_path}/{class_idx}_2.jpg'
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
            'name': f"PIS_{shifts[shift_idx]}",
            'group1': lines[class_idx]['set1'],
            'group2': lines[class_idx]['set2']
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'