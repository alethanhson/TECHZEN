Generic single-database configuration.

### 1. Tạo migration mới (Khi thêm bảng/cột, đổi kiểu dữ liệu)
```bash
docker-compose run --rm backend alembic revision --autogenerate -m "Mô tả thay đổi"
```

### 2. Cập nhật Database (Migrate)
```bash
docker-compose run --rm backend alembic upgrade head
```

### 3. Quay lại bản cũ (Rollback)
- **Lùi lại 1 bước**:
```bash
docker-compose run --rm backend alembic downgrade -1
```
- **Lùi lại n bước (VD: 2 bước)**:
```bash
docker-compose run --rm backend alembic downgrade -2
```
- **Lùi về một ID cụ thể**:
```bash
docker-compose run --rm backend alembic downgrade <revision_id>
```

### 4. Kiểm tra trạng thái
```bash
docker-compose run --rm backend alembic history --verbose
docker-compose run --rm backend alembic current
```