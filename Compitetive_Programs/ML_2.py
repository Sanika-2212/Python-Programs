import pandas as pd

Border = "-" * 70

print(Border)
print("Loading the dataset...")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(Border)
print("Total Number of Students in Dataset are:-", df.shape[0])
print(Border)

print(Border)
print("Total Number of students passed:-", (df["FinalResult"]==1).sum())
print(Border)

print(Border)
print("Total Number of students failed:-",(df["FinalResult"]==0).sum())
print(Border)
