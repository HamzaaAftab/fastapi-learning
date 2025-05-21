# Import BaseModel from pydantic
from pydantic import BaseModel
from typing import Optional
# By Default the fields we define in pydantic are required ones, meaning we have to use them, However we can also use optional fields as sometimes in our data, some fields are not required always..Pydantic provides us with this feature too.

# We can make a field optional by using the keyword 'Optional' from the typing module, 
class Patient(BaseModel):
    name: str
    age: int
    status: Optional[str] = None # This indicates that the status is of String type and is optional..

# Step 2: Now we make object of this Pydantic class
patient_info = {
    'name': 'John',
    'age': 25
}


# Now we are making the object of Patient class, since we used dictionary, we need to unpack it using **.
patient1= Patient(**patient_info)
print(patient1)


def insert_patient_data(patient: Patient):
    # Suppose we are adding this in the database
    print(f"{patient.name} and {patient.age} is added to database")
    
insert_patient_data(patient1)

# Code without pydantic...This is not ideal way because a user can change the type at runtime
# def insert_patient_data(name, age):
#     # Suppose we are adding this in the database
#     print(f"{name} and {age} is added to database")
    
# insert_patient_data("John", "20")