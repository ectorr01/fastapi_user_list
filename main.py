from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class UsernameRequest(BaseModel):
    username: str

users: List[str] = []

@app.get("/")  
def homepage():
    return "Hello, this is the homepage"

@app.post("/add-user")
def add_user(data: UsernameRequest):
    if data.username in users:
        return {"message": f"User {data.username} is already present."}
    users.append(data.username)
    return {"message": f"User {data.username} added successfully."}

@app.get("/check-user")
def check_user(username: str):
    if username in users:
        return {"exists": True, "username": username}
    else:
        return {"exists": False, "username": username}

@app.get("/total-users")
def total_users():
    return {"total": len(users)}

@app.delete("/delete-user")
def delete_user(username: str):
    if username in users:
        users.remove(username)
        return {"message": f"User {username} deleted."}
    else:
        raise HTTPException(status_code=404, detail=f"User {username} not found.")

@app.get("/list-users")
def list_users():
    return {"users": users}
