from typing import List
from fastapi import FastAPI
from uuid import uuid4
from models.User import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name="Jamila", 
        last_name="ahmad", 
        gender=Gender.female, 
        role=[Role.student]
    ),

    User(
        id=uuid4(), 
        first_name="alex", 
        last_name="Jones", 
        gender=Gender.male, 
        role=[Role.student, Role.admin]
    ),
]

@app.get("/")
def root():
    return {"Hello": "World"}