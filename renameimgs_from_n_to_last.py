import os

folder_path = "./Desktop/DeepLearning/Datasets/TEMP/"
n = 301

image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]  # Add more extensions if needed

for index, filename in enumerate(sorted(os.listdir(folder_path)), start=n):
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension in image_extensions:
        new_filename = f"{index}{file_extension}"
        new_filepath = os.path.join(folder_path, new_filename)
        old_filepath = os.path.join(folder_path, filename)
        os.rename(old_filepath, new_filepath)
        print(f"Renamed: {filename} -> {new_filename}")
