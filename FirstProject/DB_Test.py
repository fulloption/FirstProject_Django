from django.db import connection
# import settings
import os
# import django
try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')
    # django.setup()
    connection.cursor()
except Exception as e:
    print(f"Error connecting to database: {e}")
else:
    print("Successfully connected to database.")