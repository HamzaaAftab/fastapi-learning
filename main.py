from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

def load_mock_data():
    with open('mockdata.json', 'r') as f:
        data = json.load(f)
    return data
        

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
def view_patient(patient_id: str):
    data = load_data() # Load all the data first to see the particular patient exists or not
    if patient_id in data: # if the patient_id:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

# Getting Data from mockData using Params (Dynamic Route)
@app.get("/mockdata/{data_id}")
def view_data(data_id: int):
    data = load_mock_data()
    # Search for the object with matching id
    for item in data:
        if item["id"] == data_id:
            return item
    raise HTTPException(status_code=404, detail="Person not found")