import scanpy as sc

print("Loading UMAP dataset...")

adata = sc.read_h5ad("../data/adata_umap.h5ad")

# find marker genes
sc.tl.rank_genes_groups(adata, groupby="kmeans", method="wilcoxon")

print("Marker genes identified")

# plot marker genes
sc.pl.rank_genes_groups(adata, n_genes=20, sharey=False, save="_markers.png")

# save
adata.write("../data/adata_markers.h5ad")

print("Saved as adata_markers.h5ad")