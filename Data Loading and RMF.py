import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Read the data
# Update the file path to your CSV file location in Google Drive
file_path = '/content/drive/My Drive/Online Retail.csv'  
try:
    # Try reading with semicolon delimiter first
    df = pd.read_csv(file_path, encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')  
except pd.errors.ParserError:
    # If semicolon fails, try comma delimiter
    df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip')  


# 1. Initial Data Exploration
print("Dataset Shape:", df.shape)
print("\nFirst few rows:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Data Cleaning
def clean_data(df):
    # Remove rows with missing CustomerID
    df_cleaned = df.dropna(subset=['CustomerID'])
    
    # Convert CustomerID to int
    df_cleaned['CustomerID'] = df_cleaned['CustomerID'].astype(int)
    
    # Convert InvoiceDate to datetime
    df_cleaned['InvoiceDate'] = pd.to_datetime(df_cleaned['InvoiceDate'])
    
    # Calculate total amount
    df_cleaned['TotalAmount'] = df_cleaned['Quantity'] * df_cleaned['UnitPrice']
    
    # Remove cancelled orders (those starting with 'C')
    df_cleaned = df_cleaned[~df_cleaned['InvoiceNo'].astype(str).str.contains('^C', regex=True)]
    
    # Convert 'Quantity' and 'UnitPrice' to numeric, handling errors
    df_cleaned['Quantity'] = pd.to_numeric(df_cleaned['Quantity'], errors='coerce')
    df_cleaned['UnitPrice'] = pd.to_numeric(df_cleaned['UnitPrice'], errors='coerce')

    # Remove negative quantities and prices
    df_cleaned = df_cleaned[(df_cleaned['Quantity'] > 0) & (df_cleaned['UnitPrice'] > 0)]
    
    return df_cleaned

df_cleaned = clean_data(df)

# 3. Calculate RFM metrics
def calculate_rfm(df):
    # Calculate max date for recency
    max_date = df['InvoiceDate'].max()
    
    rfm = df.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (max_date - x.max()).days,  # Recency
        'InvoiceNo': 'nunique',                              # Frequency
        'TotalAmount': 'sum'                                 # Monetary
    })
    
    rfm.columns = ['Recency', 'Frequency', 'Monetary']
    return rfm

rfm = calculate_rfm(df_cleaned)

# Print RFM summary
print("\nRFM Metrics Summary:")
print(rfm.describe())

# 4. Visualize RFM distributions
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
sns.histplot(data=rfm, x='Recency', bins=30)
plt.title('Recency Distribution')

plt.subplot(1, 3, 2)
sns.histplot(data=rfm, x='Frequency', bins=30)
plt.title('Frequency Distribution')

plt.subplot(1, 3, 3)
sns.histplot(data=rfm, x='Monetary', bins=30)
plt.title('Monetary Distribution')

plt.tight_layout()
plt.show()


