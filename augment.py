import os
import random
from PIL import Image, ImageEnhance

def augment_image(input_image_path, output_image_path):
    img = Image.open(input_image_path)    
    augmentations = [
        flip_image,
        rotate_image,
        change_brightness,
        change_contrast,
    ]
    for augmentation in augmentations:
        if random.random() < 0.5:  # 50% chance of applying each augmentation
            img = augmentation(img)
    img = resize_image(img)  # Always resize to 224x224
    if img.mode == 'RGBA':
        img = img.convert('RGB')
    
    img.save(output_image_path)


def flip_image(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def rotate_image(img):
    angle = random.randint(-30, 30)  # Rotate between -30 and 30 degrees
    return img.rotate(angle)

def change_brightness(img):
    enhancer = ImageEnhance.Brightness(img)
    factor = random.uniform(0.7, 1.3)  # Brightness factor between 0.7 and 1.3
    return enhancer.enhance(factor)

def change_contrast(img):
    enhancer = ImageEnhance.Contrast(img)
    factor = random.uniform(0.7, 1.3)  # Contrast factor between 0.7 and 1.3
    return enhancer.enhance(factor)

def resize_image(img):
    return img.resize((224, 224))  # Resize to 224x224

def augment_images_in_folder(input_folder, output_folder, target_count=1000):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_list = os.listdir(input_folder)
    current_count = len(file_list)

    while current_count < target_count:
        # Randomly select an input image from the folder
        input_image_name = random.choice(file_list)
        input_image_path = os.path.join(input_folder, input_image_name)

        # Generate the output image path based on the current count
        output_image_name = f"augmented_{current_count}.jpg"
        output_image_path = os.path.join(output_folder, output_image_name)

        # Augment the image and save it to the output folder
        augment_image(input_image_path, output_image_path)
        current_count += 1

if __name__ == "__main__":
    input_folder = "./Datasets/DOCS/test/4/"
    output_folder = "./Datasets/DOCS/test/4/"
    target_count = 300

    augment_images_in_folder(input_folder, output_folder, target_count)
