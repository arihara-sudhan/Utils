import matplotlib.pyplot as plt

# Example data (replace with your own values)
epochs = [1, 2, 3, 4, 5]
accuracy = [0.85, 0.88, 0.90, 0.92, 0.94]

# Create a line plot
plt.plot(epochs, accuracy, marker='o', linestyle='-')

# Add labels and a title
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Accuracy vs. Epochs')

# Show the plot
plt.grid(True)
plt.show()
