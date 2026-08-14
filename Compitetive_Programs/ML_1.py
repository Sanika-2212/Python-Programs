import pandas as pd

Border = "-" * 70
print(Border)
print("Loading the dataset...")
print(Border)

DataPath = "student_performance_ml.csv"

df = pd.read_csv(DataPath)

print(Border)
print("First Five Records are :-\n", df.head())
print(Border)

print(Border)
print("Last Five Records are :-\n", df.tail())
print(Border)

print(Border)
print("Total Number of Rows and columns are :-\n",df.shape)
print(Border)

print(Border)
print("List of column Names is:-\n", list(df.columns))
print(Border)

print(Border)
print("Data Types of each column is:-\n",df.dtypes)
print(Border)
