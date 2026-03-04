import scanpy as sc

print("Loading HVG dataset...")

adata = sc.read_h5ad("../data/adata_hvg.h5ad")

print(adata)

# Make a real copy (avoids view warnings)
adata = adata.copy()

# Scale data (mean = 0, variance = 1)
sc.pp.scale(adata, max_value=10)

print("Scaling complete")

# Save scaled dataset
adata.write("../data/adata_scaled.h5ad")

print("Saved as adata_scaled.h5ad")