import json  # Import the JSON 


with open("file.json", "r") as file:
    data = json.load(file)  
    print(data)  

# Modify the dictionary by adding a new key&value 
data["langage"] = "Python"

# Write the modified dictionary back to the JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=2) 

with open("data.json", "r") as file:
    data = json.load(file) 
    print("\nContenu du fichier après modification :")
    print(data) 