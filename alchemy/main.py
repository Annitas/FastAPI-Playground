from fastapi import FastAPI
from fastapi.openapi.models import Response
from sqladmin import Admin, ModelView
from starlette.applications import Starlette
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from admin.views import UserAdmin
from users.models import Base

app = FastAPI(
    title="Admin App"
)














engine = create_engine(
    "sqlite:///example.db",
    connect_args={"check_same_thread": False},
)

# Base.metadata.create_all(engine)  # Create tables
admin = Admin(app, engine)

admin.add_view(UserAdmin)
