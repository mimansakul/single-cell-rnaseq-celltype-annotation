import scanpy as sc

print("Loading clustered dataset...")

adata = sc.read_h5ad("../data/adata_kmeans.h5ad")

print(adata)

# Compute neighbors for UMAP
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)

print("Neighbors computed")

# Compute UMAP
sc.tl.umap(adata)

print("UMAP computed")

# Plot clusters
sc.pl.umap(adata, color="kmeans", save="_kmeans_clusters.png")

# Plot patients
sc.pl.umap(adata, color="patient_id", save="_patients.png")

# Save dataset
adata.write("../data/adata_umap.h5ad")

print("Saved as adata_umap.h5ad")