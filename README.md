# User List with FastAPI 🚀

A simple REST API project built with FastAPI to manage a list of users.

## 🛠 Features

- Add a user  
- Check if a user exists  
- Get total number of users  
- Delete a user  
- View the full list of users  

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/user-list-fastapi.git 
   

🌐 Available Endpoints

  - POST /add-user
  - GET /check-user?username=...
  - GET /total-users
  - GET /list-users
  - DELETE /delete-user?username=...
  - 

    
📚 API Documentation
Visit http://127.0.0.1:8000/docs to test the endpoints interactively.

## 📌 Libraries

🧠 Pydantic : Data Validation in Python Pydantic is a Python library for data validation and parsing. It is widely used in web applications such as FastAPI to ensure that data received (e.g. from an HTTP request) is correctly formatted. 
Pydantic lets you define "models" for your data, and then automatically validates the input data against those models.

- 📦 BaseModel: The core class of Pydantic
BaseModel is the main Pydantic class that allows you to define schemas (models) for data. When you create a class that inherits from BaseModel, you are defining a data model.


🧠 Typing is a module included in the Python standard library since Python 3.5 and is used to add type information to variables, functions, and classes.
It allows you to specify what type of data you expect or return a certain variable or function.

## Summary

| Libraries      | Description |
| ----------- | ----------- |
| Pydantic      | Library for validating and parsing data in Python.|
| BaseModel   | Base class for defining typed data models.| |
| FastAPI + Pydantic + Typing | A powerful combination for building type-safe, auto-documented APIs with Python.|


