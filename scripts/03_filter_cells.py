import scanpy as sc

print("Loading QC dataset...")

adata = sc.read_h5ad("../data/adata_with_qc_metrics.h5ad")

print(adata)

# -----------------------------
# Filter cells
# -----------------------------

# Remove very low quality cells
adata = adata[adata.obs.n_genes_by_counts > 200, :]

# Remove potential doublets
adata = adata[adata.obs.n_genes_by_counts < 7000, :]

print("Cells after filtering:", adata.n_obs)

# -----------------------------
# Filter genes
# -----------------------------

sc.pp.filter_genes(adata, min_cells=3)

print("Genes after filtering:", adata.n_vars)

# -----------------------------
# Save filtered dataset
# -----------------------------

adata.write("../data/adata_filtered.h5ad")

print("Saved as adata_filtered.h5ad")