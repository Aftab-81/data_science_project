import json
import joblib
from pathlib import Path
"""
1. Saving data into JSON
data = {
    "name": "Aftab",
    "age": 21
}

with open("test.json", "w") as f:
    json.dump(data, f, indent = 4)

print("File created successfully")
"""

"""
2. REading data from JSON
print("Reading json from file")

with open("test.json", "rb") as f:
    content = json.load(f)
print("File reading successfull\n\n")
print(content)
"""

"""
3. Saving model into binary file
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
joblib.dump(model, Path("model.pkl"))
print(f"Model stored at: {Path('model.pkl')}")

"""

model = joblib.load("model.pkl")
print(model)
print("Model is loaded..")