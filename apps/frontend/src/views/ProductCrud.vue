<template>
  <MainLayout>
    <!-- Header: Search & Add -->
    <div class="mb-4 d-flex justify-content-between align-items-end">
      <div class="flex-grow-1 me-3">
        <h2 class="fw-bold mb-3">Quản lý Sản phẩm</h2>
        <div class="d-flex gap-2" style="max-width: 500px">
          <TInput v-model="searchQuery" placeholder="Tìm kiếm theo tên hoặc mã..." @keyup.enter="loadData" class="mb-0 flex-grow-1" />
          <TButton @click="loadData">
            <i class="bi bi-search me-1"></i> Tìm
          </TButton>
        </div>
      </div>
      <TButton variant="primary" @click="openAddModal">
        <i class="bi bi-plus-lg me-1"></i> Thêm mới
      </TButton>
    </div>

    <!-- Table -->
    <TCard no-body>
      <TTable :items="filteredItems" :fields="fields" striped hover v-model:busy="loading">
        <template #cell(is_active)="{ item }">
          <TBadge :variant="item.is_active ? 'success' : 'secondary'">
            {{ item.is_active ? 'Active' : 'Inactive' }}
          </TBadge>
        </template>

        <template #cell(price)="{ item }">
          {{ Number(item.price).toLocaleString('vi-VN') }} đ
        </template>

        <template #cell(actions)="{ item }">
          <div class="d-flex gap-2">
            <TButton variant="outline-info" size="sm" @click="openEditModal(item)">
              <i class="bi bi-pencil-square"></i>
            </TButton>
            <TButton variant="outline-danger" size="sm" @click="confirmDelete(item)">
              <i class="bi bi-trash-fill"></i>
            </TButton>
          </div>
        </template>

        <template #table-busy>
          <div class="text-center text-primary my-5">
            <TSpinner class="align-middle" />
            <strong class="ms-2">Đang tải dữ liệu...</strong>
          </div>
        </template>
      </TTable>
    </TCard>

    <!-- Modal Add/Edit -->
    <TModal
      v-model="modalVisible"
      :title="isEditMode ? 'Chỉnh sửa sản phẩm' : 'Thêm sản phẩm mới'"
      @ok="handleSave"
      size="lg"
      header-bg-variant="primary"
      header-text-variant="white"
    >
      <div class="row g-3">
        <div class="col-md-6">
          <TInput label="Mã sản phẩm" v-model="form.code" :disabled="isEditMode" />
        </div>
        <div class="col-md-6">
          <TInput label="Tên sản phẩm" v-model="form.name" />
        </div>
        <div class="col-md-6">
          <TInput label="Giá" v-model="form.price" type="number" />
        </div>
        <div class="col-md-6">
          <TInput label="Số lượng" v-model="form.quantity" type="number" />
        </div>
        <div class="col-md-12">
          <TTextarea label="Mô tả" v-model="form.description" />
        </div>
        <div class="col-md-12">
          <TCheckboxGroup label="Trạng thái" v-model="form.activeList" :options="['Kích hoạt']" />
        </div>
      </div>
    </TModal>

    <!-- Modal Delete -->
    <TModal v-model="deleteModalVisible" title="Xác nhận xóa" @ok="handleDelete" variant="danger">
      <p class="text-danger fw-bold">Bạn có chắc chắn muốn xóa sản phẩm này? Thao tác không thể hoàn tác.</p>
    </TModal>

    <!-- Toast -->
    <TToast v-model="toast.visible" :title="toast.title" :variant="toast.variant">
      {{ toast.message }}
    </TToast>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import MainLayout from '@/layouts/MainLayout.vue'
import { createCrudService } from '@/services/api'

// --- Types ---
interface Product {
  id: number
  code: string
  name: string
  description: string | null
  price: number
  quantity: number
  is_active: boolean
}

// --- API Service ---
const productApi = createCrudService<Product>('products')

// --- State ---
const items = ref<Product[]>([])
const loading = ref(false)
const searchQuery = ref('')
const modalVisible = ref(false)
const deleteModalVisible = ref(false)
const isEditMode = ref(false)
const selectedId = ref<number | null>(null)

const form = reactive({
  code: '',
  name: '',
  description: '',
  price: 0,
  quantity: 0,
  activeList: [] as string[],
})

const toast = reactive({
  visible: false,
  message: '',
  title: 'Thông báo',
  variant: 'success',
})

const fields = [
  { key: 'code', label: 'Mã SP', sortable: true },
  { key: 'name', label: 'Tên sản phẩm', sortable: true },
  { key: 'price', label: 'Giá', sortable: true },
  { key: 'quantity', label: 'Số lượng' },
  { key: 'is_active', label: 'Trạng thái' },
  { key: 'actions', label: 'Thao tác', class: 'text-center' },
]

// --- Computed ---
const filteredItems = computed(() => {
  if (!searchQuery.value) return items.value
  const q = searchQuery.value.toLowerCase()
  return items.value.filter(
    (i) => i.code.toLowerCase().includes(q) || i.name.toLowerCase().includes(q),
  )
})

// --- Actions ---
const showToast = (msg: string, variant = 'success') => {
  toast.message = msg
  toast.variant = variant
  toast.visible = true
  setTimeout(() => (toast.visible = false), 3000)
}

const resetForm = () => {
  Object.assign(form, { code: '', name: '', description: '', price: 0, quantity: 0, activeList: [] })
}

const loadData = async () => {
  loading.value = true
  try {
    items.value = await productApi.getAll()
  } catch (e: any) {
    showToast(e.message || 'Lỗi tải dữ liệu', 'danger')
  } finally {
    loading.value = false
  }
}

const openAddModal = () => {
  isEditMode.value = false
  resetForm()
  modalVisible.value = true
}

const openEditModal = (item: Product) => {
  isEditMode.value = true
  selectedId.value = item.id
  Object.assign(form, {
    code: item.code,
    name: item.name,
    description: item.description || '',
    price: item.price,
    quantity: item.quantity,
    activeList: item.is_active ? ['Kích hoạt'] : [],
  })
  modalVisible.value = true
}

const handleSave = async () => {
  const payload = {
    code: form.code,
    name: form.name,
    description: form.description || null,
    price: Number(form.price),
    quantity: Number(form.quantity),
    is_active: form.activeList.length > 0,
  }

  try {
    if (isEditMode.value && selectedId.value) {
      await productApi.update(selectedId.value, payload)
      showToast('Cập nhật thành công!')
    } else {
      await productApi.create(payload)
      showToast('Thêm mới thành công!')
    }
    await loadData()
  } catch (e: any) {
    showToast(e.message || 'Lỗi lưu dữ liệu', 'danger')
  }
}

const confirmDelete = (item: Product) => {
  selectedId.value = item.id
  deleteModalVisible.value = true
}

const handleDelete = async () => {
  if (!selectedId.value) return
  try {
    await productApi.delete(selectedId.value)
    showToast('Đã xóa thành công!')
    await loadData()
  } catch (e: any) {
    showToast(e.message || 'Lỗi xóa dữ liệu', 'danger')
  }
}

onMounted(loadData)
</script>
