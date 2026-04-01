# TECHZEN - Fullstack Recruitment Test

Dự án này là một bài kiểm tra kỹ thuật (Technical Test) dành cho vị trí phát triển Fullstack. Hệ thống bao gồm Backend (FastAPI), Frontend (Vue.js) và cơ sở dữ liệu MySQL, được điều phối thông qua Docker.

## 🚀 Công nghệ sử dụng

### Backend
- **Framework**: FastAPI (Python 3.11+)
- **Database ORM**: SQLAlchemy 2.0
- **Migration**: Alembic
- **Authentication**: JWT (JSON Web Token).
- **Validation**: Pydantic v2
- **Database**: MySQL 8.0

### Frontend
- **Framework**: Vue 3 (Composition API)
- **Build Tool**: Vite
- **Language**: TypeScript
- **Styling**: Bootstrap 5 + BootstrapVueNext
- **State Management**: VueUse + Vue Router

### Infrastructure
- **Containerization**: Docker & Docker Compose
- **Web Server/Proxy**: Nginx

---

## 📦 Cách cài đặt và khởi chạy

### 1. Yêu cầu hệ thống
- cài đặt **Docker** và **Docker Compose**.
- cài đặt **Git**.

### 2. Các bước khởi chạy
1. **Clone repository**:
   ```bash
   git clone <repository_url>
   cd TECHZEN
   ```

2. **Cấu hình môi trường**:
   Sao chép file `.env.example` thành `.env` (mặc định đã có cấu hình sẵn cho Docker):
   ```bash
   cp .env.example .env
   ```

3. **Khởi chạy bằng Docker Compose**:
   ```bash
   docker compose up --build -d
   ```
   *Lệnh này sẽ khởi chạy 4 service: `frontend`, `backend`, `db` (MySQL) và `nginx`.*

4. **Chạy Migrations (Cập nhật database)**:
   Sau khi các container đã ổn định, thực hiện migrate để tạo bảng và seed dữ liệu mẫu:
   ```bash
   docker compose exec backend alembic upgrade head
   ```

### 3. Truy cập ứng dụng
- **Frontend**: [http://localhost](http://localhost) (Nginx proxy) hoặc [http://localhost:8080](http://localhost:8080)
- **Backend API Docs**: [http://localhost/api/docs](http://localhost/api/docs)
- **MySQL**: `localhost:3306` (User: `techzen`, Pass: `password123`)

---

## 🛠 Cấu trúc dự án
- `/apps/backend`: Mã nguồn FastAPI (đã được module hóa thành `auth`, `user`, `product`).
- `/apps/frontend`: Mã nguồn Vue.js với cấu trúc nguyên tử (Atomic components).
- `/.docker`: Chứa các Dockerfile và cấu hình Nginx.
- `docker-compose.yml`: Quản lý toàn bộ hệ sinh thái dịch của dự án.

---

## 🔐 Tài khoản mặc định (Sau khi migrate)
- **Admin**: `admin@techzen.com` / `password123`
- **User**: `user@techzen.com` / `password123`
