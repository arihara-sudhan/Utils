import os
import shutil

# List of source directories containing train and test subfolders
source_directories = ["ARABIC_DOCS", "DOCS", "LANG_DOCS", "MLIMGS","TOBACCO"]
# Destination directory for unified train and test subfolders
destination_directory = "UNIFIED"

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Loop through source directories
for source_dir in source_directories:
    for split in ["train", "test"]:
        split_dir = os.path.join(source_dir, split)
        if os.path.exists(split_dir):
            for class_folder in os.listdir(split_dir):
                class_folder_path = os.path.join(split_dir, class_folder)
                if os.path.isdir(class_folder_path):
                    destination_path = os.path.join(destination_directory, split, class_folder)
                    # Move the class folder to the unified directory
                    shutil.move(class_folder_path, destination_path)
                    print(f"Moved {class_folder_path} to {destination_path}")

print("All subfolders moved to the unified directory.")
