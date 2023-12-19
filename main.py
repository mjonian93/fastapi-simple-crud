# main.py
from typing import List
from uuid import uuid4
from fastapi import FastAPI
from models import Gender, Role, User
from uuid import UUID
from fastapi import HTTPException

app = FastAPI()
db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.user],
        ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="James",
        last_name="Gabriel",
        gender=Gender.male,
        roles=[Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Eunit",
        last_name="Eunit",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
]

@app.get("/")
async def root():
    return {"Hello": "World",}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{id}")
async def delete_user(id: UUID):
   for user in db:
      if user.id == id:
         db.remove(user)
         return
      raise HTTPException(
          status_code=404, detail=f"Delete user failed, id {id} not found."
          )