# Customer-Purchase-Analysis
## Overview

This is a Customer purchase analysis modal using k-means clustering which provides an in-depth analysis of customer behaviour based on multiple parameters
The customer segments can be interpreted as:

Low recency, high frequency/monetary = Best customers
High recency, low frequency/monetary = Lost customers
Medium values = Average customers

## Analysis Methodology
1. **Data Preprocessing**
   - Handling missing values
   - Removing negative quantities and prices (likely returns)
   - Converting transaction dates to proper format
   - Creating customer-level aggregations

2. **RFM Analysis**
   - Recency: Days since last purchase
   - Frequency: Total number of purchases
   - Monetary: Total amount spent

3. **Customer Segmentation**
   - Feature scaling of RFM metrics
   - Determining optimal number of clusters
   - Applying K-means clustering
   - Profiling customer segments


## Dataset
The analysis uses the "Online Retail" dataset, which contains:
- Transaction records for a UK-based online retail company
- Data period: 2010-2011
- Features include: Invoice No, Stock Code, Description, Quantity, Price, Customer ID, and Country

## Key Features
- Customer segmentation using K-means clustering
- RFM (Recency, Frequency, Monetary) analysis
- Data preprocessing and cleaning
- Visualization of customer segments

## Technical Stack
- **Python Libraries**:
  - pandas: Data manipulation
  - scikit-learn: K-means clustering
  - matplotlib/seaborn: Visualization
  - numpy: Numerical operations
    
## Results
The analysis identifies distinct customer segments based on:
- Purchase frequency
- Average transaction value
- Total spending patterns
- Geographic distribution



Results and Findings
The analysis typically reveals distinct customer segments such as:

High-value loyal customers
Regular mid-tier customers
Occasional buyers
One-time purchasers

Future Improvements

Implement more advanced clustering algorithms
Include product category analysis
Add seasonal trend analysis
Develop predictive models for customer behavior

Visuals from the Analytics
 


<img width="1328" alt="Screenshot 2025-04-25 at 12 59 21 PM" src="https://github.com/user-attachments/assets/b1194f61-7b42-44d9-96bb-122ecb062f63" />



<img width="865" alt="Screenshot 2025-04-25 at 12 59 52 PM" src="https://github.com/user-attachments/assets/4c7878d0-18cf-4466-9977-10532dfafb2b" />


<img width="90<img width="1297" alt="Screenshot 2025-04-25 at 1 00 39 PM" src="https://github.com/user-attachments/assets/0be9c180-e31c-4a9a-a96a-9394cce7e600" />

<img width="1297" alt="Screenshot 2025-04-25 at 1 00 39 PM" src="https://github.com/user-attachments/assets/0ef0264b-c699-4656-9bde-54d9f95355be" />




<img width="1193" alt="Screenshot 2025-04-25 at 1 01 00 PM" src="https://github.com/user-attachments/assets/a3a93e76-ce73-4a33-b9ad-8439117df80a" />


<img width="1195" alt="Screenshot 2025-04-25 at 1 01 10 PM" src="https://github.com/user-attachments/assets/f1b3f473-a46b-4aec-b4da-957bfc6889a7" />

