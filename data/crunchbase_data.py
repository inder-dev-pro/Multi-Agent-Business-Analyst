import kagglehub
import pandas as pd
# Download latest version
path = kagglehub.dataset_download("yanmaksi/big-startup-secsees-fail-dataset-from-crunchbase")

print("Path to dataset files:", path)
df=pd.read_csv(path+ r"\big_startup_secsees_dataset.csv")
print(df['status'].unique())
print(df['status'].value_counts())

print(df.head())
print(df.info())
print(df.describe())