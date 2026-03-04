import scanpy as sc

print("Loading PCA dataset...")

adata = sc.read_h5ad("../data/adata_pca.h5ad")

print(adata)

# Build nearest neighbor graph
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=30)

print("Neighbor graph computed")

# Save
adata.write("../data/adata_neighbors.h5ad")

print("Saved as adata_neighbors.h5ad")