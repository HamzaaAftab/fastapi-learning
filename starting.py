from fastapi import FastAPI

app = FastAPI()

Person = {
    "Hamza": "John",
    "age": 30,
}
@app.get("/")
def hello():
    return {
        "message": "Hello World"
    }
    
@app.get("/name")
def name(name: str):
    return name