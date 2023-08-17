import os
import torch
import torchvision.transforms as transforms
import torchvision.datasets as datasets

# Define the root directory containing dataset folders
root_dir = './DSET/'

# List of dataset names
dataset_names = ['ONE', 'TWO']

# Define data transformations for preprocessing
data_transforms = {
    'train': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ]),
    'test': transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ]),
}

# Load and combine the datasets
combined_datasets = []
for dataset_name in dataset_names:
    dataset_path = os.path.join(root_dir, dataset_name)
    combined_datasets.append(datasets.ImageFolder(os.path.join(dataset_path, 'train'), data_transforms['train']))

# Concatenate the datasets
combined_dataset = torch.utils.data.ConcatDataset(combined_datasets)
# Create a data loader for combined training
combined_dataloader = torch.utils.data.DataLoader(combined_dataset, batch_size=32, shuffle=True, num_workers=4)
# Get class names from the first dataset
class_names = combined_datasets[1].classes
# Example usage of the combined dataloader
print("Number of combined images:", len(combined_dataset))
print("Class names:", class_names)
