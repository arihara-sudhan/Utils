import os
import imgaug as ia
from imgaug import augmenters as iaa
from skimage import io

# Set the path to your main "train" folder
main_folder = "./UNIFIED/train"
n_samples_per_folder = 5  # Change this to the desired number of samples per folder

# Initialize image augmenter with desired augmentation techniques
augmenter = iaa.Sequential([
    iaa.Affine(rotate=(-10, 10)),  # Rotation within -10 to 10 degrees
    iaa.Fliplr(0.5),  # Horizontal flip with a 50% chance
    iaa.Affine(translate_percent={"x": (-0.1, 0.1), "y": (-0.1, 0.1)}),  # Translation within -10% to 10%
])

# Function to augment images in a subfolder
def augment_images_in_subfolder(subfolder_path):
    image_files = [f for f in os.listdir(subfolder_path) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    
    existing_images = len(image_files)
    required_augmentations = n_samples_per_folder - existing_images
    
    if required_augmentations <= 0:
        return
    
    for i in range(required_augmentations):
        image_file = image_files[i % existing_images]
        image_path = os.path.join(subfolder_path, image_file)
        image = io.imread(image_path)

        # Perform augmentation
        augmented_image = augmenter.augment_image(image)

        # Save augmented image
        augmented_image_filename = f"augmented_{i + existing_images}_{image_file}"
        augmented_image_path = os.path.join(subfolder_path, augmented_image_filename)
        io.imsave(augmented_image_path, augmented_image)

# Iterate through subfolders and augment images
for root, dirs, files in os.walk(main_folder):
    for subfolder in dirs:
        subfolder_path = os.path.join(root, subfolder)
        augment_images_in_subfolder(subfolder_path)
