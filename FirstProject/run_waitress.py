from waitress import serve  # นำเข้า serve function จาก waitress
from FirstProject.wsgi import application  # นำเข้า WSGI application จากโปรเจกต์ Django ของคุณ

if __name__ == '__main__':
    # ใช้ serve function เพื่อรันแอปพลิเคชันบนเซิร์ฟเวอร์ Waitress
    serve(application, host='0.0.0.0', port=8001)
