import json

# Load JSON data
with open('arts', 'r') as f:
    data = json.load(f)

# Convert '2023CUTOFF' values from strings to floats, replacing "-" with 0
for entry in data:
    cutoff_value = entry.get("2023CUTOFF")
    if cutoff_value == "-":  # Replace "-" with 0
        entry["2023CUTOFF"] = 0.0
    elif cutoff_value:  # Convert valid values to float
        try:
            entry["2023CUTOFF"] = float(cutoff_value)
        except ValueError:
            print(f"Invalid value for cutoff: {cutoff_value}")

# Save updated JSON data
with open('arts.json', 'w') as f:
    json.dump(data, f, indent=4)
