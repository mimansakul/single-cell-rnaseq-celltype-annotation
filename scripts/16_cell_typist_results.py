import pandas as pd
import scanpy as sc

adata = sc.read_h5ad("../data/adata_celltypist_final.h5ad")

cell_counts = adata.obs["majority_voting"].value_counts()

cell_counts.to_csv("../data/celltype_counts.csv")

print(cell_counts)