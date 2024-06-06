From example : https://devhub.in.th/blog/django-python<br>
Project : FirstProject<br>
App : FristApp<br>


project/<br>
├── FirstApi/<br>
│   ├── __init__.py<br>
│   ├── urls.py<br>
│   ├── models.py<br>
│   ├── apps.py<br>
│   ├── admin.py<br>
│   ├── serializers.py<br>
│   └── views.py<br>
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

    FirstApi/
        FirstApi/init.py: ไฟล์นี้อ้างอิงโมดูลทั้งหมดในแอปพลิเคชัน FirstApi
        FirstApi/admin.py: ไฟล์นี้กำหนดค่าการแสดงผลข้อมูลใน Django admin
        FirstApi/apps.py: ไฟล์นี้กำหนดค่าแอปพลิเคชัน FirstApi
        FirstApi/models.py: ไฟล์นี้กำหนดโครงสร้างฐานข้อมูลสำหรับแอปพลิเคชัน FirstApi
        FirstApi/serializers.py: ไฟล์นี้แปลงข้อมูลระหว่าง Python objects กับ JSON
        FirstApi/tests.py: ไฟล์นี้เก็บ unit tests สำหรับแอปพลิเคชัน FirstApi
        FirstApi/urls.py: ไฟล์นี้กำหนด URL patterns สำหรับแอปพลิเคชัน FirstApi
        FirstApi/views.py: ไฟล์นี้เก็บ function views สำหรับแอปพลิเคชัน FirstApi

    FirstApp/
        FirstApp/migrations/: เก็บไฟล์ migrations สำหรับการเปลี่ยนแปลงฐานข้อมูล
        FirstApp/init.py: ไฟล์บอก Python ว่าไดเรกทอรีนี้เป็นแพ็กเกจ
        FirstApp/admin.py: กำหนดการจัดการข้อมูลผ่าน Django admin interface
        FirstApp/apps.py: กำหนดการตั้งค่าแอปพลิเคชัน
        FirstApp/models.py: กำหนดแบบจำลอง (models) ของข้อมูล
        FirstApp/tests.py: เขียนทดสอบต่างๆ สำหรับแอปพลิเคชัน
        FirstApp/views.py: กำหนดมุมมอง (views) สำหรับการตอบสนองต่อคำขอของผู้ใช้

    FirstProject/
        FirstProject/init.py: ไฟล์นี้บอก Python ว่าไดเรกทอรีนี้ควรได้รับการปฏิบัติเป็นแพ็กเกจ
        FirstProject/settings.py: การตั้งค่าของโปรเจกต์ เช่น ฐานข้อมูล, Static files, แอปพลิเคชันที่ติดตั้ง
        FirstProject/urls.py: กำหนด URL patterns สำหรับโปรเจกต์
        FirstProject/asgi.py: สำหรับการเชื่อมต่อ ASGI (Asynchronous Server Gateway Interface)
        FirstProject/wsgi.py: สำหรับการเชื่อมต่อ WSGI (Web Server Gateway Interface)

    manage.py: สคริปต์สำหรับการจัดการโปรเจกต์ เช่น การรันเซิร์ฟเวอร์, การทำ makemigrations,migrations 
    Run : run_waitress.py [port=8000]
    url : http://localhost:8000/ 
    