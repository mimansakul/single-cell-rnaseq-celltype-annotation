import scanpy as sc

print("Loading normalized dataset...")

adata = sc.read_h5ad("../data/adata_normalized.h5ad")

print(adata)

# Identify highly variable genes
sc.pp.highly_variable_genes(
    adata,
    flavor="seurat",
    n_top_genes=2000
)

print("Highly variable genes identified")

# Plot HVG distribution
sc.pl.highly_variable_genes(adata, save="_hvg.png")

# Keep only HVGs
adata = adata[:, adata.var.highly_variable]

print("Dataset after HVG filtering:")
print(adata)

# Save
adata.write("../data/adata_hvg.h5ad")

print("Saved as adata_hvg.h5ad")