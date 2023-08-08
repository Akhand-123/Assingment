# 2. Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file.
import json
state = {
    "Andhra Pradesh":"Amaravati",
    "Assam":"Dispur",
    "Bihar":"Patna",
    "Chhattisgarh":"Raipur",
    "Himachal Prades":"Shimla",
    "Madhya Pradesh":"Bhopal",
    "Goa":"Panaji",
}
with open("state.json","w") as f:
    json.dump(state,f,indent=4)
with open("state.json","r") as f:
    d = json.load(f)
print(d)

# Output
# {'Andhra Pradesh': 'Amaravati', 'Assam': 'Dispur', 'Bihar': 'Patna', 'Chhattisgarh': 'Raipur', 'Himachal Prades': 'Shimla', 'Madhya Pradesh': 'Bhopal', 'Goa': 'Panaji'}
     