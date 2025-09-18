import pandas as pd

data = pd.read_csv("lung_cancer_dataset.csv")

data[["copd_diagnosis", "family_history", "lung_cancer"]] = data[["copd_diagnosis", "family_history", "lung_cancer"]].replace({"Yes":1, "No":0})

avg_men = ((data["gender"] == "Male").sum() / 50000)*100
avg_female = ((data["gender"] == "Female").sum() / 50000)*100

avg_age = (data["age"].mean())

print(data)
print(avg_age)
print(avg_men)
print(avg_female)
