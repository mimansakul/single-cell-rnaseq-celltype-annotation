import scanpy as sc
import matplotlib.pyplot as plt

adata = sc.read_h5ad("../data/adata_celltypist_final.h5ad")

adata.obs["majority_voting"].value_counts().plot.bar(figsize=(10,5))

plt.ylabel("Number of Cells")
plt.xlabel("Cell Type")
plt.title("Cell Type Distribution")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()

plt.savefig("figures/celltype_distribution.png")

plt.show()