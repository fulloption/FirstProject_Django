From example : https://devhub.in.th/blog/django-python
Project : FirstProject
App : FristApp


myproject/
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── myapp/
│   ├── migrations/
│   │   └── __init__.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── manage.py
└── requirements.txt


รายละเอียดแต่ละไฟล์และไดเรกทอรี

    myproject/
        myproject/init.py: ไฟล์นี้บอก Python ว่าไดเรกทอรีนี้ควรได้รับการปฏิบัติเป็นแพ็กเกจ
        myproject/settings.py: การตั้งค่าของโปรเจกต์ เช่น ฐานข้อมูล, Static files, แอปพลิเคชันที่ติดตั้ง
        myproject/urls.py: กำหนด URL patterns สำหรับโปรเจกต์
        myproject/asgi.py: สำหรับการเชื่อมต่อ ASGI (Asynchronous Server Gateway Interface)
        myproject/wsgi.py: สำหรับการเชื่อมต่อ WSGI (Web Server Gateway Interface)

    myapp/
        myapp/migrations/: เก็บไฟล์ migrations สำหรับการเปลี่ยนแปลงฐานข้อมูล
        myapp/init.py: ไฟล์บอก Python ว่าไดเรกทอรีนี้เป็นแพ็กเกจ
        myapp/admin.py: กำหนดการจัดการข้อมูลผ่าน Django admin interface
        myapp/apps.py: กำหนดการตั้งค่าแอปพลิเคชัน
        myapp/models.py: กำหนดแบบจำลอง (models) ของข้อมูล
        myapp/tests.py: เขียนทดสอบต่างๆ สำหรับแอปพลิเคชัน
        myapp/views.py: กำหนดมุมมอง (views) สำหรับการตอบสนองต่อคำขอของผู้ใช้

    manage.py: สคริปต์สำหรับการจัดการโปรเจกต์ เช่น การรันเซิร์ฟเวอร์, การทำ migrations

    requirements.txt: ไฟล์ระบุแพ็กเกจ Python ที่จำเป็นต้องใช้ในโปรเจกต์