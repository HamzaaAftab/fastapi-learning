from fastapi import FastAPI, Path, HTTPException, Query # HTTPException is used to raise exceptions
import json
from fastapi.responses import JSONResponse # For sending JSON Response to the client
from pydantic import BaseModel, Field, computed_field # Computed fields are for calculations, Field are for validations and user experience
from typing import Annotated, Literal # for Adding Descriptions in our model

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="The ID of the patient", examples = ['P0001'])]
    name: Annotated[str, Field(..., description="The name of the patient", examples = ['John Doe'])]
    city: Annotated[str, Field(..., description="The city of the patient", examples = ['Guwahati'])]
    age: Annotated[int, Field(..., gt=0, lt=120, description="The age of the patient", examples = [25])]
    gender: Annotated[Literal["male", "female"], Field(..., description="The gender of the patient", examples = ['male'])]
    height: Annotated[float, Field(..., gt=0, description="The height of the patient", examples = [1.75])]
    weight: Annotated[float, Field(..., gt=0, description="The Weight of the patient", examples = [1.75])]
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = self.weight / (self.height ** 2)
        return round(bmi, 2)
    
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def load_mock_data():
    with open('mockdata.json', 'r') as f:
        data = json.load(f)
    return data

def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f)
        

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

# route to get data from mock data
@app.get('/mock')
def mock():
    data = load_mock_data()
    return data

# Getting from Patient ID (Dynamic Route)
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient you want to view")):
    data = load_data() # Load all the data first to see the particular patient exists or not
    if patient_id in data: # if the patient_id:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found") # Raising Custom Exception

# Getting Data from mockData using Params (Dynamic Route)
@app.get("/mockdata/{data_id}")
def view_data(data_id: int):
    data = load_mock_data()
    # Search for the object with matching id
    for item in data:
        if item["id"] == data_id:
            return item
    raise HTTPException(status_code=404, detail="Person not found")

# Query Parameters: Optional key pair values seperated by &, it is used for filtering, sorting etc.
# Query parameters use Query(...) function
@app.get("/sort")
def sort_patients(sort_by: str = Query(... , description="Sort on the basis of height, weight or bmi"), order: str = Query('asc', description="Sort in ascending or descending order")):
   
    
    valid_fields = ['height', 'weight', 'bmi']
    
    # Error Handling for both Query Parameters...
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order")
    
    data = load_data() # Load all the data first
    
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    
    return sorted_data

# POST Api
@app.post("/create")
def create_patient(patient: Patient): # patient of Patient Pydantic Class
    # load existing data
    data = load_data()
    
    # check if patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exists")
    
    # add new patient
    # data[patient.id] = patient.dict()
    data[patient.id] = patient.model_dump(exclude=['id']) # This method returns a dictionary representation of the patient object
    
    # save updated data to file
    save_data(data)
    
    return JSONResponse(status_code=202, content={"message": "Patient created successfully"})
    
    
    