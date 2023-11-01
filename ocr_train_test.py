import os
import cv2
import pytesseract

# Path to the "train" directory containing images
train_dir = "./MINI-DOCUMENTS/train"

# Path to the "train_text" directory to save extracted text
train_text_dir = "./MINI-DOCUMENTS/train_text"

# Create "train_text" directory if it doesn't exist
os.makedirs(train_text_dir, exist_ok=True)

# Recursively process subdirectories and files
for root, subdirs, files in os.walk(train_dir):
    for file in files:
        if file.lower().endswith(('.png', '.jpg','.tiff','.tif' ,'.jpeg', '.gif', '.bmp')):
            # Construct the input image path
            image_path = os.path.join(root, file)

            # Construct the corresponding output text file path
            relative_path = os.path.relpath(image_path, train_dir)
            text_file_path = os.path.join(train_text_dir, os.path.splitext(relative_path)[0] + ".txt")

            # Ensure the output directory exists
            os.makedirs(os.path.dirname(text_file_path), exist_ok=True)

            # Read the image using OpenCV
            image = cv2.imread(image_path)

            # Use Tesseract to perform OCR and extract text
            extracted_text = pytesseract.image_to_string(image)

            # Save the extracted text to a text file
            with open(text_file_path, 'w', encoding='utf-8') as text_file:
                text_file.write(extracted_text)
                print(f"Extracted text from '{image_path}' and saved to '{text_file_path}'")
