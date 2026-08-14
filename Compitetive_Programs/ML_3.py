import pandas as pd

Border = "-" * 70

print(Border)
print("Loading the dataset...")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)
print(Border)
print("Average Study Hours are:-", df["StudyHours"].mean())
print(Border)

print(Border)
print("Average Attendance is:-", df["Attendance"].mean())
print(Border)

print(Border)
print("Maximum Previous Score is:-", df["PreviousScore"].max())
print(Border)

print(Border)
print("Minimum Sleep Hours are:-", df["SleepHours"].min())
print(Border)
