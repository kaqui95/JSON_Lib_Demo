#
import json

#

data1 = {

    'name': 'Karsten',
    'age': 29,
    'city': 'Seattle',
    'interests': ['Travel', 'food', 'cars', 'sports', 'music', 'golfing'], 
    'is_student': False 
}

#
with open('data1.json','w') as json_file:

    #Dump the data dictionary into the JSON file
    json.dump(data1,json_file,indent=4)

    #Confirmation Statement
print("Data has been written to data1.json")

####
#Read the JSON file.

with open('data1.json','r') as json_file:
          

    loaded_data = json.load(json_file)

print("Successfully able to read data1.json")
print(loaded_data) 

###
#Change the contents of the JSON Dictionary.

loaded_data['age'] = 29
loaded_data['interests'].append('Happy')


#Resave the altered JSON file
with open('data1.json', 'w') as json_file:

    #Dump the data dictionary into the JSON file.
    json.dump(loaded_data, json_file, indent=4) 
    
print("Modified data written to data1.json") 
        