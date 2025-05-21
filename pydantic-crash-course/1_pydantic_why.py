# Import BaseModel from pydantic
from pydantic import BaseModel

# Step 1: Creating Pydantic Model Class
# Now in this class we will define our Ideal Schema
class Patient(BaseModel):
    name: str
    age: int

# Step 2: Now we make object of this Pydantic class
patient_info = {
    'name': 'John',
    'age': 25
}

updated_info = {
    'name': "Jenny",
    'age' : 26
}

# Now we are making the object of Patient class, since we used dictionary, we need to unpack it using **.
patient1= Patient(**patient_info)
print(patient1)

patient2= Patient(**updated_info)
print(patient2)

def insert_patient_data(patient: Patient):
    # Suppose we are adding this in the database
    print(f"{patient.name} and {patient.age} is added to database")
    
insert_patient_data(patient1)

def update_patient_data(patient:Patient):
    # Suppose we are updating this in the database
    print(f"{patient.name} and {patient.age} is updated in database")

update_patient_data(patient2)

# Code without pydantic...This is not ideal way because a user can change the type at runtime
# def insert_patient_data(name, age):
#     # Suppose we are adding this in the database
#     print(f"{name} and {age} is added to database")
    
# insert_patient_data("John", "20")