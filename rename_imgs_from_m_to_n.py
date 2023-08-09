import os

def rename_images(folder_path):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(image_extensions)]

    for idx, filename in enumerate(sorted(image_files)):
        new_name = f"{idx + 1}.jpg"
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {filename} to {new_name}")

folder_path = "/path/to/your/folder"

rename_images(folder_path)
