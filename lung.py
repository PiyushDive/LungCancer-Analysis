import pandas as pd

data = pd.read_csv("lung_cancer_dataset.csv")

print("Minimum age of lung cancer :")
if data["lung_cancer"]:
    agee = data["age"].min()