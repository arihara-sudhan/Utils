import os

def rename_folders(base_folder):
    folders = [folder for folder in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, folder))]
    folders.sort()  # Sort folders to maintain consistency in renaming
    
    class_mapping = {}
    new_class_id = 1
    
    for folder in folders:
        old_path = os.path.join(base_folder, folder)
        new_folder = str(new_class_id)
        new_path = os.path.join(base_folder, new_folder)
        
        os.rename(old_path, new_path)
        class_mapping[folder] = new_folder
        
        new_class_id += 1
        
    return class_mapping

train_folder = "./Datasets/UNIFIED/train/"
test_folder = "./Datasets/UNIFIED/test/"

train_mapping = rename_folders(train_folder)
test_mapping = rename_folders(test_folder)

print("Train folder mapping:", train_mapping)
print("Test folder mapping:", test_mapping)
