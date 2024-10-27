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


