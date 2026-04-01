# TECHZEN Recipe Book: Copy-Paste Master Guide

Bản tài liệu này tập trung vào **Syntax**, **Cách thực hiện** và **Code có thể Copy-Paste ngay**.

---

## 🏗️ Recipe 1: Thêm một Trang CRUD Mới (Ví dụ: `Category`)

### Bước 1: Backend Model (SQLAlchemy 2.0) - `apps/backend/models.py`
```python
from sqlalchemy.orm import Mapped, mapped_column
from .database import Base

class Category(Base):
    __tablename__ = "categories"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True, index=True)
    description: Mapped[str | None] = mapped_column(default=None)
```

### Bước 2: Backend Schema (Pydantic v2) - `apps/backend/schemas.py`
```python
from pydantic import BaseModel, ConfigDict

class CategoryBase(BaseModel):
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    pass

class CategoryRead(CategoryBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
```

### Bước 3: Backend Router (FastAPI) - `apps/backend/routers/categories.py`
```python
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..database import get_db
from ..models import Category
from ..schemas import CategoryRead, CategoryCreate

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("/", response_model=list[CategoryRead])
def get_all(db: Session = Depends(get_db)):
    return db.scalars(select(Category)).all()

@router.post("/", response_model=CategoryRead)
def create(item: CategoryCreate, db: Session = Depends(get_db)):
    db_item = Category(**item.model_dump())
    db.add(db_item); db.commit(); db.refresh(db_item)
    return db_item
```

### Bước 4: Frontend Component (Vue 3 + T-Atoms) - `apps/frontend/src/views/CategoryCrud.vue`
```vue
<template>
  <MainLayout>
    <div class="d-flex justify-content-between mb-3">
      <h2>Quản lý Danh mục</h2>
      <TButton variant="primary" @click="openModal">Thêm mới</TButton>
    </div>

    <TTable :items="items" :fields="fields" striped hover v-model:busy="loading">
      <template #cell(actions)="{ item }">
        <TButton size="sm" variant="outline-danger" @click="confirmDelete(item.id)">Xóa</TButton>
      </template>
    </TTable>

    <TModal v-model="modalShow" title="Thêm danh mục" @ok="handleSave">
      <TInput label="Tên danh mục" v-model="form.name" />
      <TTextarea label="Mô tả" v-model="form.description" />
    </TModal>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import { createCrudService } from '@/services/api'

const api = createCrudService<any>('categories')
const items = ref([])
const loading = ref(false)
const modalShow = ref(false)
const form = reactive({ name: '', description: '' })

const fields = [
  { key: 'id', label: 'ID' },
  { key: 'name', label: 'Tên' },
  { key: 'actions', label: 'Thao tác' }
]

const load = async () => { 
  loading.value = true; items.value = await api.getAll(); loading.value = false 
}
const openModal = () => { Object.assign(form, { name: '', description: '' }); modalShow.value = true }
const handleSave = async () => { await api.create(form); load() }
const confirmDelete = async (id: number) => { if(confirm('Chắc chắn xóa?')) { await api.delete(id); load() } }

onMounted(load)
</script>
```

---

## 🎨 Recipe 2: Common Layout Syntax (Copy & Paste Utils)

### Grid 2-Cột (Responsive)
```html
<div class="row g-3">
  <div class="col-12 col-md-6">...Cột Trái...</div>
  <div class="col-12 col-md-6">...Cột Phải...</div>
</div>
```

### Căn giữa tuyệt đối (Flexbox)
```html
<div class="d-flex justify-content-center align-items-center vh-100">
  <div>Nội dung nằm chính giữa màn hình</div>
</div>
```

### Header kèm nút Search (Standard Techzen Style)
```html
<div class="mb-4 d-flex justify-content-between align-items-center">
  <h2 class="mb-0">Tiêu đề</h2>
  <div class="d-flex gap-2">
    <TInput v-model="search" placeholder="Tìm..." class="mb-0" />
    <TButton variant="primary">Search</TButton>
  </div>
</div>
```

---

## ⚡ Recipe 3: FastAPI Queries (SQLAlchemy 2.0 Syntax)

- **Lấy 1 item theo ID**: `db.get(Model, id)`
- **Lấy danh sách có Filter**: `db.scalars(select(Model).where(Model.col == val)).all()`
- **Update nhanh**: `db.execute(update(Model).where(Model.id == id).values(col=val)); db.commit()`
- **Delete nhanh**: `db.execute(delete(Model).where(Model.id == id)); db.commit()`
- **Sắp xếp**: `select(Model).order_by(Model.created_at.desc())`
- **Phân trang (Limit/Offset)**: `select(Model).offset(10).limit(20)`

---

## 🛠️ Recipe 4: Vue 3 Common Patterns

- **Watch một giá trị**: `watch(query, () => loadData())`
- **Computed (Lọc nhanh list)**: `const filtered = computed(() => items.value.filter(i => i.name.includes(q.value)))`
- **Emit cho cha**: `const emit = defineEmits(['update']); emit('update', true)`
- **Xử lý Error Async**:
```ts
try {
  await api.call()
} catch (e: any) {
  // Toast đã được tự động hiển thị trong api.ts của bạn
  console.error(e)
}
```
