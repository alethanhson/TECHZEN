# 🚀 TECHZEN Master Offline Cheat Sheet (Everything-in-one)

## 🏗️ 1. TECHZEN UI (Frontend Atoms)
| Component | Syntax cơ bản | Ghi chú |
| :--- | :--- | :--- |
| **TInput** | `<TInput label="Tên" v-model="name" />` | Có sẵn label |
| **TButton** | `<TButton variant="primary" @click="do">` | b-button wrapper |
| **TTable** | `<TTable :items="list" :fields="f" busy />` | b-table wrapper |
| **TBadge** | `<TBadge variant="success">Active</TBadge>` | nhãn trạng thái |
| **TModal** | `<TModal v-model="show" title="X" @ok="ok">` | b-modal wrapper |
| **TCard** | `<TCard title="Title">Details</TCard>` | b-card wrapper |
| **TToast** | `<TToast v-model="v" title="Thông báo" />` | b-toast wrapper |

---

## 🐍 2. Backend (FastAPI & SQLAlchemy 2.0)
### SQLAlchemy 2.0 Select Patterns
```python
# Scalar (1 object)
stmt = select(User).where(User.id == id)
user = db.scalar(stmt) # Returns None if not found

# Scalars (List of objects)
stmt = select(Product).order_by(Product.id.desc())
products = db.scalars(stmt).all()
```

### Pydantic v2 Dump
```python
# Dump to dict: schema_obj.model_dump()
# Create DB model from schema: db_obj = User(**schema.model_dump())
```

---

## 🐳 3. OPS & Database (Docker / Alembic)
### Docker Compose
- **Rebuild & Up**: `docker compose up -d --build`
- **Stop**: `docker compose down`
- **Logs**: `docker compose logs -f [service_name]`

### Alembic (Migration) - Run inside backend container
- **Create Migration**: `docker exec -it techzen-backend-1 alembic revision --autogenerate -m "mess"`
- **Upgrade DB**: `docker exec -it techzen-backend-1 alembic upgrade head`

---

## 🔌 4. API & Communication (Axios/Fetch)
### Using `createCrudService`
```ts
import { createCrudService } from '@/services/api'
const api = createCrudService<Product>('products')

const items = await api.getAll() // GET /products
await api.create(payload)        // POST /products
await api.update(id, payload)    // PUT /products/:id
await api.delete(id)             // DELETE /products/:id
```

---

## 🧬 5. Git & Workflow
- **Quick Commit**: `git add . && git commit -m "update"`
- **Reset Code**: `git reset --hard HEAD`
- **Check Ports**: `docker ps` (Backend: 8000, Frontend: 5173, Nginx: 8080)

---

## 📚 6. Chi tiết ngôn ngữ (Language Cheat Sheets)
- **[JavaScript / ES6](file:///Users/thanhson/Documents/develop/TECHZEN/docs/js-es6-cheatsheet.md)**: Array methods (`map`, `filter`), Destructuring, Spreads, Async/Await.
- **[Python Data & JSON](file:///Users/thanhson/Documents/develop/TECHZEN/docs/python-data-cheatsheet.md)**: Dict, List, JSON parse/dump, List Comprehension.
- **[Bootstrap Utils](file:///Users/thanhson/Documents/develop/TECHZEN/docs/bootstrap-vue.md)**: CSS Utility classes (m, p, d-flex, w, h).

