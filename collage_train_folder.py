from PIL import Image, ImageDraw
import os

def create_collage(images, output_path):
    width, height = images[0].size
    collage = Image.new('RGB', (width * 3, height * 3))
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if index < len(images):
                collage.paste(images[index], (j * width, i * height))
    collage.save(output_path)

def main():
    train_folder = "./train/"
    train_collage_folder = "./train_collage/"

    # Walk through the train folder
    for root, _, files in os.walk(train_folder):
        for subfolder in root.split(os.path.sep):
            if subfolder:
                collage_folder = os.path.join(train_collage_folder, subfolder)
                os.makedirs(collage_folder, exist_ok=True)

        image_files = [os.path.join(root, file) for file in files if file.lower().endswith(('.jpg', '.jpeg', '.png', '.gif'))]

        # Create collages for each batch of 9 images
        batch = []
        for image_file in image_files:
            image = Image.open(image_file)
            batch.append(image)
            if len(batch) == 9:
                collage_name = os.path.splitext(os.path.basename(image_file))[0] + "_collage.jpg"
                collage_path = os.path.join(collage_folder, collage_name)
                create_collage(batch, collage_path)
                batch = []

        # If there are not 9 images in the last batch, repeat the last image
        while len(batch) < 9 and batch:
            batch.append(batch[-1])
        if len(batch) == 9:
            collage_name = "last_batch_collage.jpg"
            collage_path = os.path.join(collage_folder, collage_name)
            create_collage(batch, collage_path)

if __name__ == "__main__":
    main()
