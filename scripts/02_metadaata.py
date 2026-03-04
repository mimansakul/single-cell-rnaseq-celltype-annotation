import scanpy as sc

print("Loading cleaned AnnData...")

adata = sc.read_h5ad("../data/adata_raw_clean.h5ad")

print(adata)

# -----------------------------
# 1 Make names unique
# -----------------------------
adata.var_names_make_unique()
adata.obs_names_make_unique()

# -----------------------------
# 2 Add metadata
# -----------------------------

# Extract patient ID
adata.obs["patient_id"] = adata.obs_names.str.split("_").str[0]

# Dataset condition
adata.obs["condition"] = "Tumor"

# Treat patient as batch
adata.obs["batch"] = adata.obs["patient_id"]

print("Metadata added:")
print(adata.obs.head())

# -----------------------------
# 3 Detect mitochondrial genes
# -----------------------------
adata.var["mt"] = adata.var_names.str.upper().str.startswith("MT-")

print("Mitochondrial genes detected:", adata.var["mt"].sum())

# -----------------------------
# 4 Calculate QC metrics
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
# 5 QC plots
# -----------------------------

sc.pl.violin(
    adata,
    ["n_genes_by_counts", "total_counts", "pct_counts_mt"],
    jitter=0.4,
    multi_panel=True,
    save="_before_filtering.png"
)

sc.pl.scatter(
    adata,
    x="total_counts",
    y="n_genes_by_counts",
    color="pct_counts_mt",
    save="_counts_vs_genes.png"
)

# -----------------------------
# 6 Save object
# -----------------------------
adata.write("../data/adata_with_qc_metrics.h5ad")

print("Saved as adata_with_qc_metrics.h5ad")