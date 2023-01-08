from fastapi import APIRouter
from config.db import conn
from models.user import users
user = APIRouter ()

@user.get("/users")
def get_users():
    return conn.execute(users.select()).fetchall()

@user.post("/users")
def create_users(users:User):
    return "hello world 2"

@user.get("/users")
def helloworld():
    return "hello world 2"

@user.get("/users")
def helloworld():
    return "hello world 2"

@user.get("/users")
def helloworld():
    return "hello world 2"