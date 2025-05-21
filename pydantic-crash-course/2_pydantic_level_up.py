# Import BaseModel from pydantic
from pydantic import BaseModel
from typing import List, Dict
# Step 1: Creating Pydantic Model Class
# Now in this class we will define our Ideal Schema
class Patient(BaseModel):
    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] # It creates list of strings..
    contact_details: Dict[str, str] # It creates a dictionary in which key is also string and value too..

# Step 2: Now we make object of this Pydantic class
patient_info = {
    'name': 'John',
    'age': 25,
    'weight': 70.5,
    'married': True,
    'allergies': ['Peanut', 'Tree nut'],
    'contact_details': {'email': 'j@j.com', 'phone': '1234567890'} # This is dictionary
}

updated_info = {
    'name': "Jenny",
    'age' : 26,
    'weight' : 70.5,
    'married' : False,
    'allergies': ['Sunlight', 'Tree nut', 'Exceesive Sweating'],
    'contact_details': {
        'email': 'jenny@j.com',
        'phone': '1234567890',
    }
}

# Now we are making the object of Patient class, since we used dictionary, we need to unpack it using **.
patient1= Patient(**patient_info)

patient2 = Patient(**updated_info)


def insert_patient_data(patient: Patient): # A parameter named patient of type Patient
    # Suppose we are adding this in the database
    print(f"The Name of Patient is: {patient.name} \n Age is: {patient.age}, \n The weight of Patient is: {patient.weight} \n The Marital Status of Patient is: {patient.married} \n The Allergies of Patient are: {patient.allergies} \n The Contact Details of Patient are: {patient.contact_details} \n {patient.contact_details['email']} and {patient.contact_details['phone']} is added to database")
    
insert_patient_data(patient1)

def update_patient_data(patient:Patient):
    # Suppose we are updating this in the database
    print(f"\n The Name of Patient is: {patient.name} \n Age is: {patient.age}, \n The weight of Patient is: {patient.weight} \n The Marital Status of Patient is: {patient.married} \n The Allergies of Patient are: {patient.allergies} \n The Contact Details of Patient are: {patient.contact_details} \n {patient.contact_details['email']} and {patient.contact_details['phone']} is updated in database")
    

update_patient_data(patient2)

# Code without pydantic...This is not ideal way because a user can change the type at runtime
# def insert_patient_data(name, age):
#     # Suppose we are adding this in the database
#     print(f"{name} and {age} is added to database")
    
# insert_patient_data("John", "20")