import os

folder_path = "/path/to/your/folder"
prefix = "prefix_to_match"  # Specify the prefix you want to match

# List all files in the folder
file_list = os.listdir(folder_path)

# Loop through the files and delete those that start with the specified prefix
for file_name in file_list:
    if file_name.startswith(prefix):
        file_path = os.path.join(folder_path, file_name)
        os.remove(file_path)
        print(f"Deleted: {file_name}")
