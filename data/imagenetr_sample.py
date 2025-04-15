import os
import random
import shutil


id = "n02510455"
class_id = "panda"

# Define source and destination directories
source_dir = f'imagenet-r/{id}'
dest_dir = f'imagenetR/classes/{class_id}'

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# List all JPEG files in the source directory (you can adjust the extension filter if needed)
all_images = [f for f in os.listdir(source_dir) if f.lower().endswith('.jpg')]

# Check if there are enough images
if len(all_images) < 10:
    print("There are not enough images in the source directory.")
else:
    # Randomly sample 10 images
    sampled_images = random.sample(all_images, 10)

    # Copy and rename the sampled images
    for idx, image_name in enumerate(sampled_images):
        src_path = os.path.join(source_dir, image_name)
        dest_path = os.path.join(dest_dir, f"{class_id}_{idx}.jpg")
        shutil.copy(src_path, dest_path)
        print(f"Copied {src_path} to {dest_path}")
