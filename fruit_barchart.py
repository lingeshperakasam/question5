import matplotlib.pyplot as plt

# Data
X = ['Apple', 'Oranges', 'Watermelon', 'Pear']
Y = [10, 22, 1, 5]

# Create bar chart
plt.bar(X, Y)

# Add titles and labels
plt.title('Fruit Quantity Barchart')
plt.xlabel('Fruit')
plt.ylabel('Quantity')

# Set y-axis to show each increment of 1
plt.yticks(range(min(Y), max(Y)+1, 1))

# Display the plot
plt.savefig('output.png')