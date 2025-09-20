import pandas as pd

uncleaned = pd.read_csv("Data/lung_cancer_dataset.csv")
uncleaned[["copd_diagnosis", "family_history", "lung_cancer"]] = uncleaned[["copd_diagnosis", "family_history",
"lung_cancer"]].replace({"Yes":1, "No":0})

uncleaned.to_csv("Data/cleaned_lung_cancer.csv", index=False)
data = pd.read_csv("Data/cleaned_lung_cancer.csv")

# it inherits data Dataframe and has all the columns.
cancer = data[data["lung_cancer"] == 1]
nocancer = data[data["lung_cancer"] == 0]

avg_age_cancer = cancer["age"].mean()
avg_age_nocancer = nocancer["age"].mean()

avg_male_cancer = (cancer["gender"] == "Male").mean()*100
avg_female_cancer = (cancer["gender"] == "Female").mean()*100
avg_male_nocancer = (nocancer["gender"] == "Male").mean()*100
avg_female_nocancer = (nocancer["gender"] == "Female").mean()*100

# family history
familyHistoryCancer = (cancer['family_history'] == 1).mean()*100
familyHistoryNocancer = (nocancer['family_history'] == 1).mean()*100

print(data.info())
print(data.describe())
print("\nAverage Age of Lung cancer positive patients: ", avg_age_cancer)
print("Average Age of Lung cancer negative patients: ", avg_age_nocancer)
print("Percentage of Males with Lung cancer: ", avg_male_cancer)
print("Percentage of Females with Lung cancer: ", avg_female_cancer)
print("Percentage of Males without Lung cancer: ", avg_male_nocancer)
print("Percentage of Females without Lung cancer: ", avg_female_nocancer)
print("Percentage of Lung cancer patients with Family History: ", familyHistoryCancer)
print("Percentage of Non-cancer patients with Family History: ", familyHistoryNocancer)

