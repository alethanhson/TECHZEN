# Techzen UI Atomic Components Library

Hệ thống component được thiết kế riêng cho Techzen, bọc quanh `bootstrap-vue-next`.

## 🏗️ Nguyên tắc chung (Atoms)
- Tất cả component bắt đầu bằng tiền tố `T` (VD: `TButton`, `TInput`).
- Hỗ trợ đầy đủ các props của BootstrapVueNext và bổ sung các tính năng tùy chỉnh.

## 1. Thành phần căn bản
### TButton
```vue
<TButton variant="primary" @click="doSomething">Click Me</TButton>
<TButton variant="outline-danger" size="sm">Remove</TButton>
```

### TInput
Hỗ trợ `label` và `v-model` trực tiếp.
```vue
<TInput label="Tên sản phẩm" v-model="form.name" placeholder="Nhập tên..." />
<TInput type="number" label="Giá" v-model="form.price" />
```

### TCard
```vue
<TCard title="Thông tin chung" no-body>
  <div class="p-3">Nội dung...</div>
</TCard>
```

## 2. Dữ liệu & Danh sách
### TTable
Tương tự `BTable` nhưng đã được tối ưu cho giao diện Techzen.
```vue
<TTable :items="items" :fields="fields" striped hover v-model:busy="loading">
  <!-- Custom Slot -->
  <template #cell(status)="{ item }">
    <TBadge :variant="item.active ? 'success' : 'secondary'">{{ item.status }}</TBadge>
  </template>
</TTable>
```

### TBadge
```vue
<TBadge variant="info">New</TBadge>
<TBadge variant="success" pill>Active</TBadge>
```

### TSpinner
Dùng cho trạng thái loading.
```vue
<TSpinner variant="primary" small />
```

## 3. Form nâng cao
### TTextarea
```vue
<TTextarea label="Mô tả" v-model="form.desc" rows="3" />
```

### TCheckboxGroup
```vue
<TCheckboxGroup label="Quyền hạn" v-model="form.roles" :options="['Admin', 'User']" />
```

### TRadioGroup
```vue
<TRadioGroup label="Giới tính" v-model="form.gender" :options="['Nam', 'Nữ']" />
```

## 4. Phản hồi & Tương tác (Feedback)
### TModal
```vue
<TModal v-model="show" title="Xác nhận" @ok="handleOk" variant="primary">
  Bạn có chắc chắn không?
</TModal>
```

### TToast
Dùng để hiển thị thông báo góc màn hình.
```vue
<TToast v-model="toast.visible" :title="toast.title" :variant="toast.variant">
  {{ toast.message }}
</TToast>
```

### TOverlay
Dùng khi đang tải dữ liệu hoặc xử lý form.
```vue
<TOverlay :show="busy">
  <MyForm />
</TOverlay>
```

---

## 🛠️ API Service: `createCrudService`
Sử dụng factory trong `@/services/api.ts` để tạo nhanh bộ gọi API.
```ts
import { createCrudService } from '@/services/api'

interface MyItem { id: number; name: string }
const myApi = createCrudService<MyItem>('resource-name')

// Cách dùng:
const list = await myApi.getAll()
const item = await myApi.getById(1)
await myApi.create({ name: 'New' })
await myApi.update(1, { name: 'Update' })
await myApi.delete(1)
```
