import os
import shutil

def flatten_folder(root_folder):
    for folder_name, subfolders, filenames in os.walk(root_folder):
        for filename in filenames:
            source_path = os.path.join(folder_name, filename)
            destination_path = os.path.join(root_folder, filename)
            shutil.move(source_path, destination_path)
    
    # Remove empty subfolders
    for folder_name, subfolders, filenames in os.walk(root_folder, topdown=False):
        for subfolder in subfolders:
            folder_path = os.path.join(folder_name, subfolder)
            if not os.listdir(folder_path):
                os.rmdir(folder_path)

if __name__ == "__main__":
    target_folder = "./images"
    flatten_folder(target_folder)
    print("Folder flattened successfully.")
