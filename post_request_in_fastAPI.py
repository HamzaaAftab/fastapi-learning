from fastapi import FastAPI, Path, HTTPException, Query # HTTPException is used to raise exceptions
from pydantic import BaseModel, computed_field, Field
from typing import Annotated, Literal
from fastapi.responses import JSONResponse # For sending JSON Response to the client
import json

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
    
    
    