import matplotlib.pyplot as plt
# Import the pyplot module

x = [1, 2, 3, 4, 5]
y = [9,11,7,22,40]

# Create the line plot
plt.plot(x, y)

# Customize the plot
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')

# Display the plot
plt.savefig('output.png')
