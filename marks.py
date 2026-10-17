import pandas as pd
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "CHEMISTRY": [85, 72, 90, 65, 78],
    "PHYSICS": [88, 70, 55, 60, 80],
    "MATHS": [90, 75, 89, 70, 85],
    "ENGLISH": [82, 68, 88, 72, 80],
    "KISWAHILI": [80, 65, 70, 75, 78],
    "BIOLOGY": [87, 70, 70, 68, 82],
    "GEOGRAPHY": [85, 70, 90, 65, 78],
    "AGRICULTURE": [80, 65, 85, 75, 78]
}
df = pd.DataFrame(data)
df.to_excel("marks.xlsx", index=False)
print(pd.read_excel("marks.xlsx"))