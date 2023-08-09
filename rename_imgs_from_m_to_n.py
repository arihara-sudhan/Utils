import os

def rename_images(folder_path, start_number, end_number):
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_files = [filename for filename in os.listdir(folder_path) if filename.lower().endswith(image_extensions)]

    for idx, filename in enumerate(sorted(image_files)):
        if start_number <= idx <= end_number:
            new_name = f"{idx}.jpg"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join(folder_path, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_name}")


folder_path = "./Datasets/MIXED/"
starting_number = 1 # Replace with your desired starting number
ending_number = 500    # Replace with your desired ending number
rename_images(folder_path, starting_number, ending_number)
