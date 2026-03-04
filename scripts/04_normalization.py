import scanpy as sc

print("Loading filtered dataset...")

adata = sc.read_h5ad("../data/adata_filtered.h5ad")

print(adata)

# Normalize counts per cell
sc.pp.normalize_total(adata, target_sum=1e4)

print("Normalization complete")

# Log transform
sc.pp.log1p(adata)

print("Log transformation complete")

# Save normalized data
adata.write("../data/adata_normalized.h5ad")

print("Saved as adata_normalized.h5ad")