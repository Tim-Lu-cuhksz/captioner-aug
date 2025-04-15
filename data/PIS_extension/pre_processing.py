import os
from PIL import Image

shifts = ["co_occurrence_shift", "context_shift", "cultural_shift", "emotional_shift", "seasonal_shift", "viewpoint_shift"]
# idx = 0

# Path to your directory
# dir_path = f'{shifts[idx]}/'

def rename(idx):
    dir_path = f'{shifts[idx]}/'
    # Iterate over all files in the directory
    for filename in os.listdir(dir_path):
        if filename.endswith('.png'):
            # Rename: replace '-' with '_'
            new_name = filename.replace('-', '_')
            old_path = os.path.join(dir_path, filename)
            new_path = os.path.join(dir_path, new_name)
            os.rename(old_path, new_path)

            # Convert PNG to JPG
            img = Image.open(new_path).convert('RGB')  # Ensure no transparency
            jpg_name = new_name.replace('.png', '.jpg')
            jpg_path = os.path.join(dir_path, jpg_name)
            img.save(jpg_path, 'JPEG')

            # Optional: Remove original PNG
            os.remove(new_path)
        
        elif filename.endswith('.jpg'):
            # Rename: replace '-' with '_'
            new_name = filename.replace('-', '_')
            old_path = os.path.join(dir_path, filename)
            new_path = os.path.join(dir_path, new_name)
            os.rename(old_path, new_path)


            # Optional: Remove original PNG
            # os.remove(new_path)

    print("Done!")

if __name__ == '__main__':
    for i in range(len(shifts)): rename(i)