from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Initialize the FastAPI app
app = FastAPI()

# Model for incoming data
class UsernameRequest(BaseModel):
    username: str

# Temporary list to store usernames
users: List[str] = []

@app.get("/")  # API endpoint (path)
def homepage():
    return "Hello, this is the homepage"

# 1. POST Endpoint: add a user
@app.post("/add-user")
def add_user(data: UsernameRequest):
    if data.username in users:
        return {"message": f"User {data.username} is already present."}
    users.append(data.username)
    return {"message": f"User {data.username} added successfully."}

# 2. GET Endpoint: check if a user exists
@app.get("/check-user")
def check_user(username: str):
    if username in users:
        return {"exists": True, "username": username}
    else:
        return {"exists": False, "username": username}

# 3. GET Endpoint: return total number of users
@app.get("/total-users")
def total_users():
    return {"total": len(users)}

# 4. DELETE Endpoint: remove a user
@app.delete("/delete-user")
def delete_user(username: str):
    if username in users:
        users.remove(username)
        return {"message": f"User {username} deleted."}
    else:
        raise HTTPException(status_code=404, detail=f"User {username} not found.")

# 5. GET Endpoint: show the full list of users
@app.get("/list-users")
def list_users():
    return {"users": users}