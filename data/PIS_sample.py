import os
import json
import random
import shutil

def sample_jsonl_and_images(jsonl_path, images_root_dir, output_jsonl_path, output_image_dir, num_samples=7, num_images_per_set=10):
    # Step 1: Load all jsonl lines
    with open(jsonl_path, 'r') as f:
        lines = [json.loads(line) for line in f]
    # print(lines)
    # Step 2: Sample 7 lines
    sampled_indices = random.sample(range(len(lines)), num_samples)
    sampled_lines = [lines[i] for i in sampled_indices]

    # Step 3: Create output dir
    os.makedirs(output_image_dir, exist_ok=True)

    # Step 4: Write sampled jsonl
    with open(output_jsonl_path, 'w') as out_f:
        for idx in sampled_indices:
            out_f.write(json.dumps(lines[idx]) + '\n')

    # Step 5: Copy 10 images from each set directory
    for new_idx, idx in enumerate(sampled_indices):
        for suffix in ["_1", "_2"]:
            src_dir = os.path.join(images_root_dir, f"{idx}{suffix}")
            dst_dir = os.path.join(output_image_dir, f"{new_idx}{suffix}")
            os.makedirs(dst_dir, exist_ok=True)

            all_images = os.listdir(src_dir)
            sampled_images = random.sample(all_images, min(num_images_per_set, len(all_images)))

            for img_name in sampled_images:
                shutil.copy(os.path.join(src_dir, img_name), os.path.join(dst_dir, img_name))
            
            # Rename the image files for ease of processing
            files = sorted([
                f for f in os.listdir(dst_dir) 
                if f.endswith('.jpg') or f.lower().endswith('.jpeg')
            ])

            for i, filename in enumerate(files):
                old_path = os.path.join(dst_dir, filename)
                new_path = os.path.join(dst_dir, f"{i}.jpg")
                os.rename(old_path, new_path)


    print(f"Sampled {num_samples} entries and saved to {output_jsonl_path}")
    print(f"Sampled image directories saved to {output_image_dir}")

# Example usage

# i = 2
# difficulty = ['easy', 'medium', 'hard']
# sample_jsonl_and_images(
#     jsonl_path=f'pairedimagesets/webcrawl/{difficulty[i]}.jsonl',
#     images_root_dir=f'pairedimagesets/webcrawl/{difficulty[i]}',
#     output_jsonl_path=f'pairedimagesets/VisDiff/{difficulty[i]}.jsonl',
#     output_image_dir=f'pairedimagesets/VisDiff/{difficulty[i]}',
#     num_samples=20
# )

if __name__ == '__main__':
    difficulty = ['easy', 'medium', 'hard']
    for i in range(len(difficulty)):
        sample_jsonl_and_images(
            jsonl_path=f'pairedimagesets/webcrawl/{difficulty[i]}.jsonl',
            images_root_dir=f'pairedimagesets/webcrawl/{difficulty[i]}',
            output_jsonl_path=f'pairedimagesets/VisDiff/{difficulty[i]}.jsonl',
            output_image_dir=f'pairedimagesets/VisDiff/{difficulty[i]}',
            num_samples=21
        )