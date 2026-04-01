# Ops Cheat Sheet: Docker, Alembic & Git

Bao gồm các lệnh cần thiết để quản lý dự án TECHZEN khi đang offline.

## 🐳 Docker Compose
Quản lý hệ thống backend, frontend, mysql, nginx trong dự án.

- **Khởi động hệ thống**: `docker compose up -d`
- **Khởi động kèm rebuild**: `docker compose up -d --build`
- **Dừng hệ thống**: `docker compose down`
- **Dừng và xóa volume (dữ liệu DB)**: `docker compose down -v`
- **Xem log toàn bộ**: `docker compose logs -f`
- **Xem log backend**: `docker compose logs -f backend`
- **Kiểm tra trạng thái container**: `docker ps`

## 🧪 Quản lý Database (Alembic)
Dự án sử dụng Alembic để quản lý migration database.

- **Khởi tạo migration (khi sửa Model)**:
  `docker exec -it techzen-backend-1 alembic revision --autogenerate -m "thay đổi gì đó"`
- **Cập nhật database lên bản mới nhất**:
  `docker exec -it techzen-backend-1 alembic upgrade head`
- **Lùi lại 1 version**:
  `docker exec -it techzen-backend-1 alembic downgrade -1`
- **Xem lịch sử các bản cập nhật**:
  `docker exec -it techzen-backend-1 alembic history`

## 🏗️ MySQL Commands
Khi cần truy cập trực tiếp MySQL DB trong container:

- **Mở shell mysql**:
  `docker exec -it mysql_db mysql -u root -p`
- **Sử dụng DB dự án**: `USE techzen_db;`
- **Xem các bảng**: `SHOW TABLES;`

## 📦 Git (Offline Workflow)
Mặc dù offline nhưng bạn vẫn nên commit code thường xuyên để lưu lịch sử.

- **Commit kèm mô tả**: `git add . && git commit -m "mô tả thay đổi"`
- **Xem trạng thái**: `git status`
- **Lùi lại commit trước (xóa thay đổi code)**: `git reset --hard HEAD`
- **Lưu tạm thay đổi (Stash)**: `git stash push -m "mess"` | `git stash pop` (Lấy lại)

---

## 🛠️ Common Fixes (Sửa lỗi thường gặp)
### 1. Frontend: Reinstall dependencies (sau khi sửa package.json)
`docker exec -it techzen-frontend-1 npm install`

### 2. Backend: Cài đặt thêm thư viện python mới
Sửa `apps/backend/requirements.txt` sau đó:
`docker compose up -d --build backend`

### 3. Sửa lỗi CORS (Nginx/Backend)
Kiểm tra cấu hình Nginx trong `docker/nginx/nginx.conf` và CORS middleware trong `apps/backend/main.py`.
