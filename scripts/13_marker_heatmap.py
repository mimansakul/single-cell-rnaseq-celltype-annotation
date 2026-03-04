import scanpy as sc

print("Loading marker dataset...")

adata = sc.read_h5ad("../data/adata_markers.h5ad")

# Plot heatmap of top marker genes
sc.pl.rank_genes_groups_heatmap(
    adata,
    groupby="kmeans",
    n_genes=5,
    save="_marker_heatmap.png"
)

print("Heatmap created")