Single-Cell RNA-seq Cell Type Annotation Pipeline

This project implements a complete single-cell RNA sequencing (scRNA-seq) analysis pipeline using Python.

The workflow performs:

preprocessing

dimensionality reduction

clustering

marker gene identification

automated cell type annotation

The pipeline is implemented using Scanpy and CellTypist, demonstrating a typical workflow used in modern single-cell transcriptomics analysis.

Dataset

Dataset: GSE103322
Source: Gene Expression Omnibus (GEO)

This dataset contains single-cell RNA sequencing data from Head and Neck Squamous Cell Carcinoma (HNSCC) tumor samples.

It includes thousands of individual cells collected from tumor microenvironments and allows researchers to study cellular heterogeneity within cancer tissues.

Dataset Publication

Puram SV et al.
Single-cell transcriptomic analysis of primary and metastatic tumor ecosystems in head and neck cancer.
Nature Genetics, 2017

Dataset Characteristics

~6000 single cells

~23,000 genes

Tumor epithelial cells

Immune cells

Stromal cells

Objective of the Project

The goal of this project is to construct a reproducible single-cell RNA-seq analysis pipeline that:

Processes scRNA-seq expression data

Identifies transcriptionally distinct cell populations

Detects cluster-specific marker genes

Annotates cell types using machine learning models

This workflow replicates the typical bioinformatics pipeline used in cancer single-cell analysis studies.

Analysis Workflow

The analysis follows a standard Scanpy scRNA-seq pipeline.

1. Data Loading

The gene expression matrix is loaded and converted into an AnnData object, the core data structure used in Scanpy.

2. Quality Control (QC)

Quality metrics are calculated to remove low-quality cells.

QC steps include:

filtering cells with very low gene counts

removing potential doublets

examining mitochondrial gene expression

3. Data Normalization

Gene expression values are normalized to make cells comparable.

This ensures sequencing depth differences do not bias downstream analysis.

4. Log Transformation

Log transformation stabilizes variance and improves statistical analysis.

5. Highly Variable Gene (HVG) Selection

Highly variable genes capture biological differences between cells and are used for dimensionality reduction.

6. Data Scaling

The data is scaled so each gene has:

mean = 0

variance = 1

This improves PCA performance.

7. Principal Component Analysis (PCA)

PCA reduces the dimensionality of the dataset while preserving major biological variation.

8. Neighborhood Graph Construction

A k-nearest neighbor graph is constructed based on PCA coordinates to represent cell-to-cell similarity.

9. Clustering

Cells are grouped into clusters representing transcriptionally similar populations.

10. UMAP Visualization

UMAP visualizes high-dimensional data in two dimensions, enabling clear visualization of clusters.

11. Marker Gene Identification

Marker genes are identified for each cluster to characterize biological identity.

12. Cell Type Annotation

Cell types are automatically predicted using CellTypist, a machine learning model trained on reference single-cell datasets.

Cluster labels are refined using majority voting.

Results

The analysis identified multiple cell populations across 5501 single cells.

Major cell populations detected include:

Basal epithelial tumor cells

CD8 effector memory T cells

CD4 regulatory T cells

Fibroblasts

Endothelial cells

Macrophages and dendritic cells

These results highlight the heterogeneous tumor microenvironment of HNSCC, consisting of epithelial tumor cells, immune infiltrates, and stromal cell populations.

Tools and Libraries Used

The following tools were used:

Python

Scanpy

CellTypist

Pandas

NumPy

Matplotlib

These tools are widely used in single-cell transcriptomics and bioinformatics research.

## Project Structure

```
scRNAseq-project

├── scripts
│   ├── 01_load_data.py
│   ├── 02_quality_control.py
│   ├── 03_normalization.py
│   ├── 04_hvg_selection.py
│   ├── 05_scaling.py
│   ├── 06_pca.py
│   ├── 07_neighbors.py
│   ├── 08_clustering.py
│   ├── 09_umap.py
│   ├── 10_marker_genes.py
│   ├── 11_celltypist_annotation.py
│   └── 12_cell_type_distribution.py

├── figures
│   ├── umap_clusters.png
│   ├── celltype_distribution.png
│   └── marker_heatmap.png

├── results
│   ├── marker_genes.xlsx
│   ├── cluster_marker_genes.xlsx
│   └── celltype_counts.xlsx

├── data
│   └── (large files ignored via .gitignore)

└── README.md
```
Outputs Generated

The pipeline produces:

UMAP visualization of cell clusters

Marker gene tables for each cluster

Cell type annotation results

Cell type distribution plots

These outputs help interpret the cellular composition of tumor samples.

Biological Significance

Single-cell RNA sequencing enables researchers to study:

tumor heterogeneity

immune infiltration

stromal cell populations

tumor microenvironment interactions

In HNSCC tumors, different cell populations such as:

malignant epithelial cells

T cells

macrophages

fibroblasts

endothelial cells

can be identified and analyzed separately.

Pipeline Workflow
Raw Data
↓
Quality Control
↓
Normalization
↓
Highly Variable Gene Selection
↓
Principal Component Analysis (PCA)
↓
Clustering
↓
UMAP Visualization
↓
Marker Gene Identification
↓
Cell Type Annotation (CellTypist)
Requirements

Python 3.8

Required libraries:

pip install scanpy celltypist pandas numpy matplotlib
Author

Mimansa Kulshrestha
MSc Bioinformatics




