# Define the path to the featnames file (e.g., "698.featnames")
featnames_file = "facebook_data/facebook/698.featnames"

# Create a dictionary to map attribute numbers to their names
attribute_mapping = {}

# Read the featnames file and populate the attribute mapping dictionary
with open(featnames_file, "r") as f:
    for line in f:
        parts = line.strip().split(" ")
        attribute_number = int(parts[0])
        attribute_name = parts[1]
        attribute_mapping[attribute_number] = attribute_name

# Print the attribute mapping
for attribute_number, attribute_name in attribute_mapping.items():
    print(f"Attribute {attribute_number}: {attribute_name}")
