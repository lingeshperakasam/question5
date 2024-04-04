import matplotlib.pyplot as plt
import numpy as np

# Generate random data (replace with your actual data)
np.random.seed(19680801)
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6] 
y_data = [7, 8, 2, 4, 7, 11, 15, 7, 10, 8, 4, 2, 7]

# Create the scatter plot
plt.scatter(x_data, y_data, alpha=0.7, c='b', marker='X', label='Data')

# Customize the plot
plt.xticks(range(21))
plt.yticks(range(21))
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')
plt.grid(True)
plt.legend()

# Display the plot
plt.savefig('output.png')