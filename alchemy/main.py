from fastapi import FastAPI
from fastapi.openapi.models import Response
from fastapi_users import fastapi_users, FastAPIUsers
from sqladmin import Admin, ModelView
from starlette.applications import Starlette
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from admin.views import UserAdmin
from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="Admin App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)











engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)

# Base.metadata.create_all(engine)  # Create tables
admin = Admin(app, engine)

admin.add_view(UserAdmin)
