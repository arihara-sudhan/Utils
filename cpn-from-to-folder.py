import os
import random
import shutil

def copy_random_images(source_dir, destination_dir, n):
    for class_folder in os.listdir(source_dir):
        class_source_dir = os.path.join(source_dir, class_folder)
        class_dest_dir = os.path.join(destination_dir, class_folder)
        if not os.path.exists(class_dest_dir):
            os.makedirs(class_dest_dir)
        image_files = [file for file in os.listdir(class_source_dir) if file.endswith('.jpg') or file.endswith('.png')]
        random.shuffle(image_files)
        for i in range(min(n, len(image_files))):
            image_file = image_files[i]
            source_path = os.path.join(class_source_dir, image_file)
            destination_path = os.path.join(class_dest_dir, image_file)
            shutil.copy(source_path, destination_path)

if __name__ == "__main__":
    train_folder = "./Datasets/DOCS_V1/train"
    val_folder = "./Datasets/DOCS_V1/val"
    n_random_images = 50
    copy_random_images(train_folder, val_folder, n_random_images)
