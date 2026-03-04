import scanpy as sc
import numpy as np

print("Loading cleaned AnnData...")

adata = sc.read_h5ad("../data/adata_raw_clean.h5ad")

print(adata)

# -----------------------------
# 1️⃣ Basic cleanup
# -----------------------------
adata.var_names_make_unique()
adata.obs_names_make_unique()

# -----------------------------
# 2️⃣ Add metadata
# -----------------------------

# Extract patient ID from cell names
# Example: HN28_P15_D06_S330_comb → HN28
adata.obs["patient_id"] = adata.obs_names.str.split("_").str[0]

# This dataset is tumor-only
adata.obs["condition"] = "Tumor"

# Treat patient as batch
adata.obs["batch"] = adata.obs["patient_id"]

print("Metadata added:")
print(adata.obs.head())

# -----------------------------
# 3️⃣ Define mitochondrial genes
# -----------------------------
adata.var["mt"] = adata.var_names.str.upper().str.startswith("MT-")

print("Number of mitochondrial genes:", adata.var["mt"].sum())

# -----------------------------
# 4️⃣ Calculate QC metrics
# -----------------------------
sc.pp.calculate_qc_metrics(
    adata,
    qc_vars=["mt"],
    percent_top=None,
    log1p=False,
    inplace=True
)

print("QC metrics calculated.")

# -----------------------------
# 5️⃣ QC PLOTS (Before filtering)
# -----------------------------

sc.pl.violin(
    adata,
    ['n_genes_by_counts', 'total_counts', 'pct_counts_mt'],
    groupby='patient_id',
    jitter=0.4,
    multi_panel=True,
    save="_before_filtering.png"
)

sc.pl.scatter(
    adata,
    x='total_counts',
    y='n_genes_by_counts',
    color='pct_counts_mt',
    save="_before_filtering.png"
)

# -----------------------------
# 6️⃣ Save updated object
# -----------------------------
adata.write("../data/adata_with_qc_metrics.h5ad")

print("Saved as adata_with_qc_metrics.h5ad")
