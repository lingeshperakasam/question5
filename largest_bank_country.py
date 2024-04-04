import pandas as pd
import matplotlib.pyplot as plt
import os

# Get the current directory path
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the CSV file
csv_file_path = os.path.join(current_directory, 'Largest-Banks.csv')

# Load the dataset
df = pd.read_csv(csv_file_path, encoding='ISO-8859-1')

# Group by 'Country' and sum the 'Total assets 2022 (US$ billion)'
country_assets = df.groupby('Country')['Total assets 2022 (USD\xa0billion)'].sum().sort_values()

# Plotting the bar chart
plt.figure(figsize=(10, 8))
country_assets.plot(kind='barh')

# Set y-axis to show increments of 500
max_assets = country_assets.max()
plt.xticks(range(0, int(max_assets) + 2500, 2500))

plt.xlabel('Total assets 2022 (USD\xa0billion)')
plt.ylabel('Country')
plt.title('Total Assets by Banks in a Country in 2022')

# Display the bar chart
plt.tight_layout()
plt.savefig('output.png')
