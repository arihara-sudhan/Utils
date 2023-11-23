import matplotlib.pyplot as plt
import torch

def disp(tensor1, tensor2, tensor3):
    image1 = tensor1.numpy() if isinstance(tensor1, torch.Tensor) else tensor1
    image2 = tensor2.numpy() if isinstance(tensor2, torch.Tensor) else tensor2
    image3 = tensor3.numpy() if isinstance(tensor3, torch.Tensor) else tensor3
    if image1.shape[1] == 1:
        image1 = image1[:, 0]
    if image2.shape[1] == 1:
        image2 = image2[:, 0]
    if image3.shape[1] == 1:
        image3 = image3[:, 0]
    if len(image1.shape) == 4:
        image1 = image1[0]
    if len(image2.shape) == 4:
        image2 = image2[0]
    if len(image3.shape) == 4:
        image3 = image3[0]
    plt.figure(figsize=(9, 3))
    plt.subplot(1, 3, 1)
    plt.imshow(image1.transpose(1, 2, 0) if len(image1.shape) == 3 else image1, cmap='gray', interpolation='nearest')
    plt.title("Tensor 1")
    plt.axis('off')

    # Plot the second image
    plt.subplot(1, 3, 2)
    plt.imshow(image2.transpose(1, 2, 0) if len(image2.shape) == 3 else image2, cmap='gray', interpolation='nearest')
    plt.title("Tensor 2")
    plt.axis('off')

    # Plot the third image
    plt.subplot(1, 3, 3)
    plt.imshow(image3.transpose(1, 2, 0) if len(image3.shape) == 3 else image3, cmap='gray', interpolation='nearest')
    plt.title("Tensor 3")
    plt.axis('off')

    # Show the plot
    plt.show()

# Example usage:
# Assuming you have three tensors named tensor1, tensor2, and tensor3
# Replace them with your actual tensors
# disp(tensor1, tensor2, tensor3)
