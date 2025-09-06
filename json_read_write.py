"""
📌Problem Statement
Create a Python script that:
1. Reads data from JSON files
2. Loops through a list of items
3. Extracts nested values
4. Merges multiple JSON files without overlap
"""

import json

# -------------------------------------------------
# Read First JSON file
with open("data1.json", 'r') as f:
    data1 = json.load(f)
    print("\nOrinigal Data1:")
    print(data1)

# Loop through a list of items (skills)
print("\nSkills List:")
for skill in data1["skills"]:
    print("-", skill)

# Extract nested values (experience details)
print("\nExtracted Nested Values:")
print("Role:", data1["experience"]["role"])
print("Years of Experience:", data1["experience"]["years"])
print("Company:", data1["experience"]["company"])

# Modify data(Example: add a new key)
data1["status"] = "processed"

# Write to a new JSON file
with open("updated_data1.json","w") as f:
    json.dump(data1, f, indent=4)

print("\nUpdated JSON1 saved!")

# -------------------------------------------------
# Read Second JSON file
with open("data2.json", "r") as f:
    data2 = json.load(f)
    print("\nOriginal Data2:")
    print(data2)

# Loop through a list of itesm (skills)
print("\nSkill List:")
for skill in data2["skills"]:
    print("-", skill)

# Extract nested values (experience details)
print("\nExtracted Nested Values:")
print("Role", data2["experience"]["role"])
print("Years of experience", data2["experience"]["years"])
print("Company", data2["experience"]["company"])

# Midify data(Example: add new key)
data2["status"] = "rejected"

# Write to a new JSON file
with open("updated_data2.json", "w") as f:
    json.dump(data2, f, indent=4)
print("\nUpdated JSON2 saved")

# ----------------------------------------------------
# Merge without overlap (put both objects into a list)
merged_data=[data1, data2]

# Save merged JSON
with open("merged_data.json", "w") as f:
    json.dump(merged_data, f, indent=4)
print("\nMerged JSON saved merged_data.json")
print("\nMerged Data")
print(merged_data)