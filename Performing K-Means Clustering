 5. Prepare data for clustering
# Handle skewness using log transformation
rfm_log = rfm.copy()

# Convert 'Monetary' and 'Frequency' columns to numeric if they are not
rfm_log['Monetary'] = pd.to_numeric(rfm_log['Monetary'], errors='coerce')
rfm_log['Frequency'] = pd.to_numeric(rfm_log['Frequency'], errors='coerce')

# Now apply log1p transformation
rfm_log['Monetary'] = np.log1p(rfm_log['Monetary'])
rfm_log['Frequency'] = np.log1p(rfm_log['Frequency'])

# ***Check and handle NaN values before scaling***
# Instead of dropping rows, keep track of the original index
original_index = rfm_log.index
rfm_log.dropna(inplace=True)  # Drop rows with NaN values

# Scale the features
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm_log)
rfm_scaled = pd.DataFrame(rfm_scaled, index=rfm_log.index, columns=rfm_log.columns)


# 6. Find optimal number of clusters using elbow method
inertias = []
K = range(1, 11)

for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(rfm_scaled)
    inertias.append(kmeans.inertia_)

# Plot elbow curve
plt.figure(figsize=(10, 6))
plt.plot(K, inertias, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# 7. Perform K-means clustering
n_clusters = 5  # You can adjust this based on the elbow curve
kmeans = KMeans(n_clusters=n_clusters, random_state=42)
# Fit and predict on the scaled data with the preserved index
cluster_labels = kmeans.fit_predict(rfm_scaled)

# Create a temporary DataFrame to store cluster labels with the preserved index
cluster_df = pd.DataFrame({'Cluster': cluster_labels}, index=rfm_log.index)

# Realign the cluster labels with the original DataFrame using the original index
rfm['Cluster'] = cluster_df.reindex(original_index)['Cluster']
## 8. Analyze clusters
# Calculate cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers = pd.DataFrame(cluster_centers, columns=rfm_log.columns)

# Plot cluster centers
plt.figure(figsize=(12, 6))
sns.heatmap(cluster_centers, annot=True, cmap='YlOrRd', fmt='.2f')
plt.title('Cluster Centers Characteristics')
plt.show()

# Calculate cluster statistics
# Ensure 'Monetary', 'Frequency', and 'Recency' are numeric
rfm['Monetary'] = pd.to_numeric(rfm['Monetary'], errors='coerce')
rfm['Frequency'] = pd.to_numeric(rfm['Frequency'], errors='coerce')
rfm['Recency'] = pd.to_numeric(rfm['Recency'], errors='coerce')

# Now calculate cluster statistics
cluster_stats = rfm.groupby('Cluster').agg({
    'Recency': 'mean',
    'Frequency': 'mean',
    'Monetary': ['mean', 'count']
}).round(2)

print("\nCluster Statistics:")
print(cluster_stats)
