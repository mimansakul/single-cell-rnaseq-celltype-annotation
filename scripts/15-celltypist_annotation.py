import scanpy as sc
import celltypist
import numpy as np
from scipy.sparse import issparse

print("Loading dataset...")

adata = sc.read_h5ad("../data/adata_markers.h5ad")

# Restore raw expression matrix if available
if adata.raw is not None:
    print("Restoring raw expression matrix")
    adata = adata.raw.to_adata()

# Convert sparse matrix to dense
if issparse(adata.X):
    adata.X = adata.X.toarray()

# Clean matrix
adata.X = np.nan_to_num(adata.X, nan=0.0)
adata.X = np.clip(adata.X, a_min=0, a_max=None)

print("Matrix cleaned")

# Normalize and log transform (required for CellTypist)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)

print("Running CellTypist annotation...")

predictions = celltypist.annotate(
    adata,
    model="Cells_Adult_Breast.pkl",
    majority_voting=True
)

print("Prediction finished")

# Convert predictions to AnnData
adata_ct = predictions.to_adata()

# Compute UMAP if missing
if "X_umap" not in adata_ct.obsm:
    sc.pp.neighbors(adata_ct)
    sc.tl.umap(adata_ct)

# Plot cell type annotation
sc.pl.umap(
    adata_ct,
    color=["predicted_labels", "majority_voting"],
    legend_loc="on data",
    save="_celltypist_annotation.png"
)

# Save annotated dataset
adata_ct.write("../data/adata_celltypist_final.h5ad")

print("CellTypist annotation completed")
print("Saved dataset: ../data/adata_celltypist_final.h5ad")