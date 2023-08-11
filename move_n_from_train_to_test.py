import os
import shutil

def move_files(source_folder, destination_folder, num_files):
    for class_folder in os.listdir(source_folder):
        class_source_path = os.path.join(source_folder, class_folder)
        class_dest_path = os.path.join(destination_folder, class_folder)

        if os.path.isdir(class_source_path):
            os.makedirs(class_dest_path, exist_ok=True)
            files_to_move = os.listdir(class_source_path)[:num_files]

            for file_name in files_to_move:
                source_file_path = os.path.join(class_source_path, file_name)
                dest_file_path = os.path.join(class_dest_path, file_name)
                shutil.move(source_file_path, dest_file_path)
                print(f"Moved: {source_file_path} to {dest_file_path}")

train_folder = "./train"
test_folder = "./test"
num_files_to_move = 100  # Number of files to move from each subfolder

move_files(train_folder, test_folder, num_files_to_move)
print("Files moved from train to test folders.")
