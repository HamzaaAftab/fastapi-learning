from fastapi import FastAPI, Path, HTTPException, Query # HTTPException is used to raise exceptions
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
    