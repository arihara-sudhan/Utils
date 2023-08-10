import os
from PIL import Image

def resize_images(input_folder, output_folder, target_size):
    for root, dirs, files in os.walk(input_folder):
        rel_path = os.path.relpath(root, input_folder)
        output_subfolder = os.path.join(output_folder, rel_path)
        
        if not os.path.exists(output_subfolder):
            os.makedirs(output_subfolder)
        
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_subfolder, file)
                
                img = Image.open(input_path)
                img = img.resize(target_size, Image.ANTIALIAS)
                img.save(output_path)

input_folder = "./Datasets/DOCS2/"
output_folder = "./Datasets/DOCS2RES/"
target_size = (500, 500)  # Set your desired target size here

resize_images(input_folder, output_folder, target_size)
