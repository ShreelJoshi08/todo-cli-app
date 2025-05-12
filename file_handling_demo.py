import json
import csv
import pandas as pd
from openpyxl import Workbook

# JSON
data = {"name": "Shreel", "role": "Intern"}
with open("data.json", "w") as f:
    json.dump(data, f)

# CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Role"])
    writer.writerow(["Shreel", "Intern"])

# TXT
with open("data.txt", "w") as f:
    f.write("Welcome to Agevole internship!\n")

# Excel
wb = Workbook()
ws = wb.active
ws.append(["Name", "Role"])
ws.append(["Shreel", "Intern"])
wb.save("data.xlsx")
