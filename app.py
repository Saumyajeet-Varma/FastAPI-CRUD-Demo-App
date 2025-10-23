from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    branch: str

users: List[User] = [] 

@app.get("/")
def index():
    return {"message": "Welcome to FastAPI"}

@app.get("/users")
def get_users():
    return users

@app.post("/user/create")
def create_user(user: User):
    users.append(user)
    return users

@app.put("/user/{user_id}")
def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return updated_user
    return {"error": "User not found"}

@app.delete("/user/delete/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    return {"error": "User not found"}