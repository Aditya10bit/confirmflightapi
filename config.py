import os

class Config:
    # Database credentials
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'  # Replace with your MySQL username
    MYSQL_PASSWORD = 'Aditya10!'  # Replace with your MySQL password
    MYSQL_DB = 'flight_db'  # Replace with the name of your database
    SECRET_KEY = os.getenv('SECRET_KEY', '6a2c3d9e1f6b4d2c5e9f8a7b6c1a0d4e')  # Fallback to a default key if not set
