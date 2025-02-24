import kagglehub

# Download latest version
path = kagglehub.dataset_download("chhinna/crunchbase-data")

print("Path to dataset files:", path)