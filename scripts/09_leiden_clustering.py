import scanpy as sc
from sklearn.cluster import KMeans

print("Loading PCA dataset...")

adata = sc.read_h5ad("../data/adata_pca.h5ad")
print(adata)

# Use the PCA coordinates for clustering
X = adata.obsm["X_pca"][:, :30]   # first 30 PCs

print("Running KMeans clustering...")
kmeans = KMeans(n_clusters=10, random_state=0, n_init=10)
labels = kmeans.fit_predict(X)

# Store cluster labels in AnnData
adata.obs["kmeans"] = labels.astype(str)

print("KMeans clustering completed")

# Save dataset
adata.write("../data/adata_kmeans.h5ad")
print("Saved as adata_kmeans.h5ad")