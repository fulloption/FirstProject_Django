From example : https://devhub.in.th/blog/django-python<br>
Project : FirstProject<br>
App : FristApp<br>


project/<br>
├── FirstProject/<br>
│   ├── __init__.py<br>
│   ├── settings.py<br>
│   ├── urls.py<br>
│   ├── asgi.py<br>
│   └── wsgi.py<br>
├── FirstApp/<br>
│   ├── migrations/<br>
│   │   └── __init__.py<br>
│   ├── __init__.py<br>
│   ├── admin.py<br>
│   ├── apps.py<br>
│   ├── models.py<br>
│   ├── tests.py<br>
│   └── views.py<br>
└── manage.py<br> 


รายละเอียดแต่ละไฟล์และไดเรกทอรี

    FirstProject/
        FirstProject/init.py: ไฟล์นี้บอก Python ว่าไดเรกทอรีนี้ควรได้รับการปฏิบัติเป็นแพ็กเกจ
        FirstProject/settings.py: การตั้งค่าของโปรเจกต์ เช่น ฐานข้อมูล, Static files, แอปพลิเคชันที่ติดตั้ง
        FirstProject/urls.py: กำหนด URL patterns สำหรับโปรเจกต์
        FirstProject/asgi.py: สำหรับการเชื่อมต่อ ASGI (Asynchronous Server Gateway Interface)
        FirstProject/wsgi.py: สำหรับการเชื่อมต่อ WSGI (Web Server Gateway Interface)

    FirstApp/
        FirstApp/migrations/: เก็บไฟล์ migrations สำหรับการเปลี่ยนแปลงฐานข้อมูล
        FirstApp/init.py: ไฟล์บอก Python ว่าไดเรกทอรีนี้เป็นแพ็กเกจ
        FirstApp/admin.py: กำหนดการจัดการข้อมูลผ่าน Django admin interface
        FirstApp/apps.py: กำหนดการตั้งค่าแอปพลิเคชัน
        FirstApp/models.py: กำหนดแบบจำลอง (models) ของข้อมูล
        FirstApp/tests.py: เขียนทดสอบต่างๆ สำหรับแอปพลิเคชัน
        FirstApp/views.py: กำหนดมุมมอง (views) สำหรับการตอบสนองต่อคำขอของผู้ใช้

    manage.py: สคริปต์สำหรับการจัดการโปรเจกต์ เช่น การรันเซิร์ฟเวอร์, การทำ migrations

    