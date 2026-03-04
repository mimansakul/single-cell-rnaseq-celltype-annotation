import scanpy as sc
import pandas as pd

print("Loading marker dataset...")

adata = sc.read_h5ad("../data/adata_markers.h5ad")

# Extract marker genes
markers = sc.get.rank_genes_groups_df(adata, group=None)

# Save to CSV
markers.to_csv("../data/marker_genes.csv", index=False)

print("Marker genes saved as marker_genes.csv")