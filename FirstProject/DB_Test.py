from django.db import connection

try:
    connection.cursor()
except Exception as e:
    print(f"Error connecting to database: {e}")
else:
    print("Successfully connected to database.")