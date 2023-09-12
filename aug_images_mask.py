import os
from PIL import Image

def rotate_image(image, angle):
    return image.rotate(angle, expand=True, resample=Image.BILINEAR)

def process_images_and_save(input_folder, output_folder, prefix, rotation_count):

    os.makedirs(output_folder, exist_ok=True)

    files = os.listdir(input_folder)
    files_with_digits = [file_name for file_name in files if any(char.isdigit() for char in file_name)]
    files_with_digits.sort(key=lambda x: int(''.join(filter(str.isdigit, x))))

    for i, file_name in enumerate(files_with_digits):

        input_path = os.path.join(input_folder, file_name)

        for j in range(rotation_count):

            angle = j * (360 // rotation_count)  # Calculate rotation angle
            output_path = os.path.join(output_folder, f"{prefix}-aug{i}_rot{angle}.png")

            image = Image.open(input_path)
            rotated_image = rotate_image(image, angle)
            rotated_image.save(output_path, 'PNG')

bleeding_folder = "./Datasets/WCEBleedGen/bleeding"  # Replace with the actual path to your "bleeding" folder
images_folder = os.path.join(bleeding_folder, "images")
annotation_folder = os.path.join(bleeding_folder, "annotation")

rotation_count = 10  # Adjust this count as needed

process_images_and_save(images_folder, os.path.join(bleeding_folder, "img-aug"), "image", rotation_count)
process_images_and_save(annotation_folder, os.path.join(bleeding_folder, "ann-aug"), "ann", rotation_count)
