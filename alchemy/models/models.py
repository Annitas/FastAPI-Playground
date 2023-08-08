from sqlalchemy import MetaData, Table, Column, Integer, Boolean, String, ForeignKey, TIMESTAMP, JSON
from datetime import datetime

metadata = MetaData()

newsletter = Table(
    "newsletter",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False)
)

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", String, nullable=False),
    Column("is_premium_subscribed", Boolean, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("newsletter_id", Integer, ForeignKey(newsletter.c.id)),
    Column("is_active", Boolean, nullable=False),
    Column("is_superuser", Boolean, nullable=False),
    Column("is_verified", Boolean, nullable=False)
)
