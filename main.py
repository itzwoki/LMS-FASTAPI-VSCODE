from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
title="FAST API LMS",
description="LMS for Managing Students and Courses.",
contact={
    "name": "M.Waqas",
    "email": "abdullahwaqas22@gmail.com"

},
license_info={
    "name": "Associate Software Engineer"
}

)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None
    id: int

@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/create-user")
async def add_user(name : User):
    users.append(name)
    return {"message" : "User {name} added."}

@app.get("/get-user/{id}")
async def get_user(id: int = Path(..., description="Enter the Id of User you want to retreive." , gt=0)):
    return users[id]