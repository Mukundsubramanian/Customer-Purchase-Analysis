9.visualize clusters in 3D
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(rfm['Recency'], 
                    rfm['Frequency'], 
                    rfm['Monetary'],
                    c=rfm['Cluster'], 
                    cmap='viridis')
ax.set_xlabel('Recency')
ax.set_ylabel('Frequency')
ax.set_zlabel('Monetary')
plt.colorbar(scatter)
plt.title('3D Cluster Visualization')
plt.show()

# 10. Customer Segmentation Interpretation
# Add segment labels based on RFM values
def get_segment_label(row):
    if row['Recency'] <= rfm['Recency'].quantile(0.25):
        if row['Frequency'] > rfm['Frequency'].quantile(0.75):
            return 'Loyal Customers'
        else:
            return 'Recent Customers'
    elif row['Recency'] > rfm['Recency'].quantile(0.75):
        if row['Frequency'] > rfm['Frequency'].quantile(0.75):
            return 'Lost High-Value Customers'
        else:
            return 'Lost Customers'
    else:
        return 'Average Customers'

rfm['Customer_Segment'] = rfm.apply(get_segment_label, axis=1)

# Print segment distribution
print("\nCustomer Segment Distribution:")
print(rfm['Customer_Segment'].value_counts())

# 11. Export results
rfm.to_csv('customer_segments.csv')
files.download('customer_segments.csv')  # This will download the results

# Print summary of each cluster
print("\nCluster Summaries:")
for cluster in range(n_clusters):
    print(f"\nCluster {cluster}:")
    cluster_data = rfm[rfm['Cluster'] == cluster]
    print(f"Number of customers: {len(cluster_data)}")
    print(f"Average Recency: {cluster_data['Recency'].mean():.2f} days")
    print(f"Average Frequency: {cluster_data['Frequency'].mean():.2f} orders")
    print(f"Average Monetary Value: ${cluster_data['Monetary'].mean():.2f}")
    print(f"Common segments: {cluster_data['Customer_Segment'].value_counts().head()}")
