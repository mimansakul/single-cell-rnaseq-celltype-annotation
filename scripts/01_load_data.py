import scanpy as sc
import pandas as pd
import numpy as np

print("Loading HNSCC dataset...")

file_path = "../data/HNSCC_all_data.txt"

# -----------------------------
# 1. Read dataset
# -----------------------------
df = pd.read_csv(file_path, sep="\t", low_memory=False)

print("Original shape:", df.shape)

# -----------------------------
# 2. Set gene column as index
# -----------------------------
df.set_index(df.columns[0], inplace=True)

# -----------------------------
# 3. Remove metadata rows
# (first rows contain annotations)
# -----------------------------
df = df.iloc[5:]

# -----------------------------
# 4. Clean gene names
# remove extra quotes
# -----------------------------
df.index = df.index.str.replace("'", "")
df.index = df.index.str.strip()

# -----------------------------
# 5. Convert to numeric
# -----------------------------
df = df.apply(pd.to_numeric, errors="coerce")

# Remove rows with no expression values
df = df.dropna(how="all")

print("After cleaning:", df.shape)

# -----------------------------
# 6. Transpose matrix
# cells x genes
# -----------------------------
df = df.T

print("After transpose:", df.shape)

# -----------------------------
# 7. Create AnnData object
# -----------------------------
adata = sc.AnnData(df)

# Make names unique
adata.var_names_make_unique()
adata.obs_names_make_unique()

print("AnnData object created:")
print(adata)

# -----------------------------
# 8. Save clean dataset
# -----------------------------
adata.write("../data/adata_raw_clean.h5ad")

print("Saved file: adata_raw_clean.h5ad")