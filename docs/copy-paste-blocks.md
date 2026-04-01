# Techzen Copy-Paste Master Blocks

Sử dụng các khối code này để xây dựng nhanh các tính năng lặp đi lặp lại.

## 🔑 1. Authentication (Login / Logout)
### Cách dùng Auth Store (`@/store/auth.ts`)
```ts
import { useAuth } from '@/store/auth'
const { state, setToken, setUser, logout } = useAuth()

// Kiểm tra login: state.value.isAuthenticated
// Lấy user: state.value.user
```

### Trang Login Mẫu
```vue
<template>
  <div class="d-flex justify-content-center align-items-center vh-100 bg-light">
    <TCard class="p-4" style="width: 400px">
      <h3 class="text-center mb-4">Đăng nhập TECHZEN</h3>
      <TInput label="Email" v-model="form.email" />
      <TInput label="Mật khẩu" type="password" v-model="form.password" @keyup.enter="handleLogin" />
      <TButton variant="primary" class="w-100 mt-3" @click="handleLogin" :disabled="loading">
        <TSpinner v-if="loading" small /> Đăng nhập
      </TButton>
    </TCard>
  </div>
</template>

<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useAuth } from '@/store/auth'
import axios from 'axios'

const form = reactive({ email: '', password: '' })
const loading = ref(false)
const { setToken, setUser } = useAuth()

const handleLogin = async () => {
  loading.value = true
  try {
    const { data } = await axios.post('/api/auth/login', form)
    setToken(data.access_token)
    setUser(data.user)
    router.push('/')
  } finally { loading.value = false }
}
</script>
```

---

## 🏗️ 2. Backend CRUD Template (A-Z)

### Model có quan hệ (SQLAlchemy)
```python
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    posts: Mapped[list["Post"]] = relationship(back_populates="author")

class Post(Base):
    __tablename__ = "posts"
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    author: Mapped["User"] = relationship(back_populates="posts")
```

### FastAPI CRUD logic tiêu chuẩn (Copy-Rename)
```python
# Create
@router.post("/")
def create_item(obj_in: MySchema, db: Session = Depends(get_db)):
    db_obj = MyModel(**obj_in.model_dump())
    db.add(db_obj); db.commit(); db.refresh(db_obj)
    return db_obj

# Update
@router.put("/{id}")
def update_item(id: int, obj_in: MySchema, db: Session = Depends(get_db)):
    db_obj = db.get(MyModel, id)
    if not db_obj: raise HTTPException(404)
    update_data = obj_in.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_obj, key, value)
    db.add(db_obj); db.commit(); db.refresh(db_obj)
    return db_obj
```

---

## ⚡ 3. FastAPI Query Patterns (Nâng cao)

- **Filter nhiều điều kiện**:
  `select(User).where(User.is_active == True, User.age > 18)`
- **Like (Tìm kiếm)**:
  `select(User).where(User.name.ilike(f"%{search_query}%"))`
- **Count**: 
  `db.scalar(select(func.count(User.id)))`
- **Join**:
  `select(Post).join(Post.author).where(User.id == 1)`

---

## 🎨 4. Bootstrap 5 Utility - Copy-Paste Patterns

- **Danh sách tin nhắn (Badge + Text)**:
  `<div class="d-flex justify-content-between"><span>Title</span><TBadge>99+</TBadge></div>`
- **Form Row (Inline)**:
  `<div class="row align-items-center"><div class="col-auto">Label</div><div class="col flex-grow-1"><TInput /></div></div>`
- **Skeleton Loading View**:
  `<div class="p-4"><TSpinner class="d-block mx-auto" /></div>`
