import kagglehub
import pandas as pd
# Download latest version
path = kagglehub.dataset_download("yanmaksi/big-startup-secsees-fail-dataset-from-crunchbase")

print("Path to dataset files:", path)
df=pd.read_csv(path+ r"\acq.csv")
print(df.head(3))
print(df.info())
print(df.describe())
print(df.columns)
print(df.isnull().sum())
print(df.duplicated().sum())