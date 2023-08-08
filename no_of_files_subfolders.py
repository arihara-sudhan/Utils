import os
folder_path = "./Datasets/DOCS_V1/train/"

# Get a list of subfolders in the specified folder
subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

# Iterate through the subfolders and count the number of files in each
for subfolder in subfolders:
    subfolder_path = os.path.join(folder_path, subfolder)
    num_files = len([filename for filename in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, filename))])
    print(f"Subfolder: {subfolder}, Number of Files: {num_files}")
