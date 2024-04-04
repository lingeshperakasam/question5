import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read the CSV files
credit_card_df = pd.read_csv(r'C:\Users\tbxbu\Desktop\Take Home Assessment\Question 1\credit_card_complaints.csv')
bank_account_df = pd.read_csv(r'C:\Users\tbxbu\Desktop\Take Home Assessment\Question 1\bank_account_or_service_complaints.csv')

# Define the response types of interest
response_types = [
    'Closed with explanation',
    'Closed',
    'Closed with monetary relief',
    'Closed with non-monetary relief'
]

# Filter the dataframes for the response types of interest
credit_card_responses = credit_card_df[credit_card_df['company_response_to_consumer'].isin(response_types)]
bank_account_responses = bank_account_df[bank_account_df['company_response_to_consumer'].isin(response_types)]

# Count the occurrences of each response type
credit_card_counts = credit_card_responses['company_response_to_consumer'].value_counts().reindex(response_types, fill_value=0)
bank_account_counts = bank_account_responses['company_response_to_consumer'].value_counts().reindex(response_types, fill_value=0)

# Set the positions for the bars
positions = np.arange(len(response_types))

# Plotting the bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the bars for credit card complaints
plt.bar(positions - 0.2, credit_card_counts, width=0.4, label='Credit Card Complaints', color='blue')

# Plot the bars for bank account complaints
plt.bar(positions + 0.2, bank_account_counts, width=0.4, label='Bank Account or Service Complaints', color='red')

# Adding the labels and title
plt.xlabel('Company Response to Consumer')
plt.ylabel('Number of Responses')
plt.title('Comparison of Company Responses to Consumer Complaints')
plt.xticks(positions, response_types, rotation=45)

# Set y-axis to show increments of 1000
plt.yticks(np.arange(0, max(credit_card_counts.max(), bank_account_counts.max()) + 2500, 2500))

# Adding the legend
plt.legend()

# Display the bar chart
plt.tight_layout()
plt.savefig('output.png')
