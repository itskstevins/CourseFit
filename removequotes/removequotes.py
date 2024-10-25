import json

# Load JSON data
with open('actuarial_yourgpt.json', 'r') as f:
    data = json.load(f)

# Convert '2023CUTOFF' values from strings to floats
for entry in data:
    if entry.get("2023CUTOFF"):
        entry["2023CUTOFF"] = float(entry["2023CUTOFF"])

# Save updated JSON data
with open('actuarial_yourgpt_updated.json', 'w') as f:
    json.dump(data, f, indent=4)