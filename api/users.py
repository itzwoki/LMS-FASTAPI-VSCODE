import fastapi 
from fastapi import Path
from typing import Optional, List
from pydantic import BaseModel


router = fastapi.APIRouter()

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None
    id: int


def generate_id() -> int:
    return len(users) + 1 if users else 1

@router.get("/users", response_model=List[User])
async def get_users():
    return users

@router.post("/create-user")
async def add_user(user : User):
    user.id = generate_id()
    users.append(user)
    return {"message" : "User {name} added."}

@router.get("/get-user/{id}")
async def get_user(
    id: int = Path(..., description="Enter the Id of User you want to retreive." , gt=0)
):
    for user in users:
        if user.id == id:
            return user
    return {"error": "user not found"}