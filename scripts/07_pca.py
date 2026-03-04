import scanpy as sc

print("Loading scaled dataset...")

adata = sc.read_h5ad("../data/adata_scaled.h5ad")

print(adata)

# Run PCA
sc.tl.pca(adata, svd_solver="arpack")

print("PCA completed")

# Plot PCA variance explained
sc.pl.pca_variance_ratio(adata, log=True, save="_pca_variance.png")

# Optional PCA scatter
sc.pl.pca(adata, color="patient_id", save="_pca_patients.png")

# Save PCA dataset
adata.write("../data/adata_pca.h5ad")

print("Saved as adata_pca.h5ad")