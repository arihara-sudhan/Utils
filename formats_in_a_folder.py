import os

folder_path = "./zohocorp_"  # Replace with the path to your folder

# Create a set to store unique file extensions
file_formats = set()

# Iterate through the files in the folder
for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_extension = os.path.splitext(filename)[1]
        file_formats.add(file_extension)

# Print the unique file formats
for format in file_formats:
    print(format)
