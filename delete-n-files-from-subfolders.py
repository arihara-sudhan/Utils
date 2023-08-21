import os
import random

# Define the folder path
folder_path = '/path/to/your/folder'

# Number of files to delete from each subfolder (m)
m = 5

# Function to delete m random files from a subfolder
def delete_random_files(subfolder_path, m):
    files_to_delete = os.listdir(subfolder_path)
    if len(files_to_delete) <= m:
        print(f"Skipping folder '{subfolder_path}' as it has fewer than {m} files.")
        return

    files_to_delete = random.sample(files_to_delete, m)

    for file_name in files_to_delete:
        file_path = os.path.join(subfolder_path, file_name)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting '{file_path}': {str(e)}")

# Iterate through subfolders in the main folder
for root, subfolders, _ in os.walk(folder_path):
    for subfolder in subfolders:
        subfolder_path = os.path.join(root, subfolder)
        delete_random_files(subfolder_path, m)
