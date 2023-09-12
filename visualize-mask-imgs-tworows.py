import os
import matplotlib.pyplot as plt
from PIL import Image
def select_and_stack_images(input_folder1, input_folder2, num_images):
    # Get a list of files in each input folder
    files1 = os.listdir(input_folder1)
    files2 = os.listdir(input_folder2)
    # Sort the files
    files1.sort()
    files2.sort()
    # Select the first num_images from each folder
    selected_files1 = files1[:num_images]
    selected_files2 = files2[:num_images]
    # Open and load images
    images1 = [Image.open(os.path.join(input_folder1, file)) for file in selected_files1]
    images2 = [Image.open(os.path.join(input_folder2, file)) for file in selected_files2]
    # Get image dimensions
    width, height = images1[0].size
    # Create a figure with subplots for stacked images
    fig, axes = plt.subplots(2, num_images, figsize=(12, 6))
    # Plot images in subplots
    for i in range(num_images):
        axes[0, i].imshow(images1[i])
        axes[0, i].axis('off')
        axes[1, i].imshow(images2[i])
        axes[1, i].axis('off')

    plt.tight_layout()
    plt.show()

images_folder = "./Datasets/WCEBleedGen/bleeding/img-aug"  # Replace with the actual path to your "images" folder
annotation_folder = "./Datasets/WCEBleedGen/bleeding/ann-aug"  # Replace with the actual path to your "annotation" folder
num_images_to_select = 4

select_and_stack_images(images_folder, annotation_folder, num_images_to_select)
