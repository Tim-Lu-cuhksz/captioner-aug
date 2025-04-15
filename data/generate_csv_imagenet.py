import csv
import yaml

# classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
# classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']

def write_to_csv_and_yaml(
        class_idx1 = 0,
        class_idx2 = 0,
        task = 'styles', # classes
        n_samples_per_set = 10
):
    assert class_idx1 < class_idx2
    base_path = f'./data/imagenetR/{task}'
    # base_path = f'./data/imagenetR/imagenetR-blurred/{task}'

    if task == 'classes':
        name_aux = 'imagenet_class'
        classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']
    elif task == 'styles':
        name_aux = 'imagenet_style'
        classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
    else:
        raise NotImplementedError

    output_csv = f'./data/{name_aux}'
    output_yaml = './configs/imagenetR'

    rows = []
    class1 = classes[class_idx1]
    class2 = classes[class_idx2]

    # For class1 images: ./data/class1/class1_0.jpg, ..., ./data/class1/class1_9.jpg
    for i in range(n_samples_per_set):
        path = f'{base_path}/{class1}/{class1}_{i}.jpg'
        rows.append({"group_name": f"{class1}", "path": path})

    for i in range(n_samples_per_set):
        path = f'{base_path}/{class2}/{class2}_{i}.jpg'
        rows.append({"group_name": f"{class2}", "path": path})
    
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")
    
    data = {
        'data': {
            'name': name_aux,
            'group1': class1,
            'group2': class2
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_blur(
        class_idx1 = 0,
        class_idx2 = 0,
        task = 'styles', # classes
        n_samples_per_set = 10
):
    assert class_idx1 < class_idx2
    # base_path = f'./data/imagenetR/{task}'
    base_path = f'./data/imagenetR/imagenetR-blurred/{task}'

    if task == 'classes':
        name_aux = 'imagenet_class'
        classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']
    elif task == 'styles':
        name_aux = 'imagenet_style'
        classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
    else:
        raise NotImplementedError

    output_csv = f'./data/{name_aux}'
    output_yaml = './configs/imagenetR'

    rows = []
    class1 = classes[class_idx1]
    class2 = classes[class_idx2]

    # For class1 images: ./data/class1/class1_0.jpg, ..., ./data/class1/class1_9.jpg
    for i in range(n_samples_per_set):
        path = f'{base_path}/{class1}/{class1}_{i}.jpg'
        rows.append({"group_name": f"Blurry {class1}", "path": path})

    for i in range(n_samples_per_set):
        path = f'{base_path}/{class2}/{class2}_{i}.jpg'
        rows.append({"group_name": f"Blurry {class2}", "path": path})
    
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")
    
    data = {
        'data': {
            'name': name_aux,
            'group1': "Blurry " + class1,
            'group2': "Blurry " + class2
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_gaussian(
        class_idx1 = 0,
        class_idx2 = 0,
        task = 'styles', # classes
        n_samples_per_set = 10
):
    assert class_idx1 < class_idx2
    # base_path = f'./data/imagenetR/{task}'
    base_path = f'./data/imagenetR/imagenetR-gaussian/{task}'

    if task == 'classes':
        name_aux = 'imagenet_class'
        classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']
    elif task == 'styles':
        name_aux = 'imagenet_style'
        classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
    else:
        raise NotImplementedError

    output_csv = f'./data/{name_aux}'
    output_yaml = './configs/imagenetR'

    rows = []
    class1 = classes[class_idx1]
    class2 = classes[class_idx2]

    # For class1 images: ./data/class1/class1_0.jpg, ..., ./data/class1/class1_9.jpg
    for i in range(n_samples_per_set):
        path = f'{base_path}/{class1}/{class1}_{i}.jpg'
        rows.append({"group_name": f"{class1} with Gaussian noise", "path": path})

    for i in range(n_samples_per_set):
        path = f'{base_path}/{class2}/{class2}_{i}.jpg'
        rows.append({"group_name": f"{class2} with Gaussian noise", "path": path})
    
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")
    
    data = {
        'data': {
            'name': name_aux,
            'group1': class1 + " with Gaussian noise",
            'group2': class2 + " with Gaussian noise"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_sp(
        class_idx1 = 0,
        class_idx2 = 0,
        task = 'styles', # classes
        n_samples_per_set = 10
):
    assert class_idx1 < class_idx2 and task in ['styles', 'classes']
    # base_path = f'./data/imagenetR/{task}'
    base_path = f'./data/imagenetR/imagenetR-sp/{task}'

    if task == 'classes':
        name_aux = 'imagenet_class'
        classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']
    elif task == 'styles':
        name_aux = 'imagenet_style'
        classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
    else:
        raise NotImplementedError

    output_csv = f'./data/{name_aux}'
    output_yaml = './configs/imagenetR'

    rows = []
    class1 = classes[class_idx1]
    class2 = classes[class_idx2]

    # For class1 images: ./data/class1/class1_0.jpg, ..., ./data/class1/class1_9.jpg
    for i in range(n_samples_per_set):
        path = f'{base_path}/{class1}/{class1}_{i}.jpg'
        rows.append({"group_name": f"{class1} with salt and pepper noise", "path": path})

    for i in range(n_samples_per_set):
        path = f'{base_path}/{class2}/{class2}_{i}.jpg'
        rows.append({"group_name": f"{class2} with salt and pepper noise", "path": path})
    
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")
    
    data = {
        'data': {
            'name': name_aux,
            'group1': class1 + " with salt and pepper noise",
            'group2': class2 + " with salt and pepper noise"
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'

def write_to_csv_and_yaml_brighten(
        class_idx1 = 0,
        class_idx2 = 0,
        task = 'styles', # classes
        n_samples_per_set = 10
):
    assert class_idx1 < class_idx2 and task in ['styles', 'classes']
    # base_path = f'./data/imagenetR/{task}'
    base_path = f'./data/imagenetR/imagenetR-brightened/{task}'

    if task == 'classes':
        name_aux = 'imagenet_class'
        classes = ['axolotl', 'flamingo', 'goldfinch', 'goldfish', 'lighthouse', 'panda', 'vulture']
    elif task == 'styles':
        name_aux = 'imagenet_style'
        classes = ['art', 'cartoon', 'deviantart', 'painting', 'sketch', 'graffiti', 'sculpture']
    else:
        raise NotImplementedError

    output_csv = f'./data/{name_aux}'
    output_yaml = './configs/imagenetR'

    rows = []
    class1 = classes[class_idx1]
    class2 = classes[class_idx2]

    # For class1 images: ./data/class1/class1_0.jpg, ..., ./data/class1/class1_9.jpg
    for i in range(n_samples_per_set):
        path = f'{base_path}/{class1}/{class1}_{i}_brightened.jpg'
        rows.append({"group_name": f"Brightened {class1}", "path": path})

    for i in range(n_samples_per_set):
        path = f'{base_path}/{class2}/{class2}_{i}_brightened.jpg'
        rows.append({"group_name": f"Brightened {class2}", "path": path})
    
    with open(f'{output_csv}.csv', 'w', newline='') as csvfile:
        fieldnames = ['group_name', 'path']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"CSV file '{output_csv}.csv' has been created with the image paths.")
    
    data = {
        'data': {
            'name': name_aux,
            'group1': "Brightened " + class1,
            'group2': "Brightened " + class2
        }
    }

    # Write to a YAML file
    with open(f'{output_yaml}.yaml', 'w') as file:
        yaml.dump(data, file, default_flow_style=False)
    print(f"yaml file '{output_yaml}.yaml' has been created with the image paths.")
    return f'{output_yaml}.yaml'