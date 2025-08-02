import os

# Use MySQL or PostgreSQL by changing the URI
SQLALCHEMY_DATABASE_URI = os.getenv(
    "DATABASE_URI", "mysql://user:password@localhost/bookstore_db"
)

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/bookstore_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False