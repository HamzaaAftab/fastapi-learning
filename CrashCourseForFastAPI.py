# Developing API's using FastAPI (CRUD Operations)
from fastapi import FastAPI
from pydantic import BaseModel # Pydantic is a Data Validation Library..
from typing import List


app = FastAPI() # Initialize FastAPI

# Basically BaseModel have the standards defined already, we it checks our data on that
# Data Validation is done using Pydantic..
# It is like making a schema for our data.
class Tea(BaseModel):
    id: int
    name: str
    origin: str

teas: List[Tea] = [] # Now we have made an empty list named teas, the type of this List is List as we imported it from typing module. and the type of each element is Tea.. 

# What is Decorators? They are something that gives superpower to your functions.. For example: if someone visits /tea, then it will print "Hello World" or something.

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/teas")
def read_tea():
    return teas

@app.post("/teas")
def create_tea(tea: Tea): # tea is an object of class Tea
    teas.append(tea) # The data of tea will be appended in Teas List and it will be return
    return tea

@app.get("/teas/{id}")
def read_tea(id: int):
    for tea in teas:
        if tea.id == id:
            return tea
    return {"message": "Tea not found"}

@app.put("/teas/{id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            teas[index] = updated_tea
            return teas[index]
    return {"message": "Tea not found"}

@app.delete("/teas/{id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return {"message": "Tea deleted"}
    return {"message": "Tea not found"}



