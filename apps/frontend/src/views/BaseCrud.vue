<template>
  <MainLayout>
    <!-- Header Page: Search & Add -->
    <div class="mb-4 d-flex justify-content-between align-items-end">
      <div class="flex-grow-1 me-3">
        <h2 class="fw-bold mb-3">Quản lý Tài khoản</h2>
        <div class="d-flex gap-2" style="max-width: 500px">
          <TInput 
             v-model="searchQuery" 
             placeholder="Tìm kiếm theo tên hoặc mã..." 
             @keyup.enter="handleSearch"
             class="mb-0 flex-grow-1"
          />
          <TButton @click="handleSearch">
             <i class="bi bi-search me-1"></i> Tìm
          </TButton>
        </div>
      </div>
      <TButton variant="primary" @click="openAddModal">
         <i class="bi bi-plus-lg me-1"></i> Thêm mới
      </TButton>
    </div>

    <!-- Table Section -->
    <TCard no-body>
      <TTable :items="items" :fields="fields" striped hover v-model:busy="loading">
        <!-- Custom slot cho cột Actions -->
        <template #cell(actions)="{ item }">
          <div class="d-flex gap-2">
            <TButton variant="outline-info" size="sm" @click="editItem(item)">
               <i class="bi bi-pencil-square"></i>
            </TButton>
            <TButton variant="outline-danger" size="sm" @click="confirmDelete(item)">
               <i class="bi bi-trash-fill"></i>
            </TButton>
          </div>
        </template>
        
        <!-- Hiển thị Loading state -->
        <template #table-busy>
          <div class="text-center text-primary my-5">
            <TSpinner class="align-middle" />
            <strong class="ms-2">Đang tải dữ liệu...</strong>
          </div>
        </template>
      </TTable>
      
      <!-- Pagination (Mẫu nếu cần) -->
      <div class="p-3 border-top d-flex justify-content-center">
         <TPagination v-model="currentPage" :total-rows="totalRows" :per-page="perPage" />
      </div>
    </TCard>

    <!-- Modal Add/Edit (Reuse) -->
    <TModal 
      v-model="modalVisible" 
      :title="isEditMode ? 'Chỉnh sửa thông tin' : 'Thêm mới dữ liệu'"
      @ok="handleSave"
      size="lg"
      header-bg-variant="primary"
      header-text-variant="white"
    >
      <div class="row g-3">
         <div class="col-md-6">
            <TInput label="Mã đối tượng" v-model="formData.code" :state="!!formData.code" feedback="Bắt buộc nhập" />
         </div>
         <div class="col-md-6">
            <TInput label="Tên đối tượng" v-model="formData.name" />
         </div>
         <div class="col-md-12">
            <TSelect label="Phân loại" v-model="formData.type" :options="typeOptions" />
         </div>
         <div class="col-md-12">
            <TTextarea label="Ghi chú" v-model="formData.note" />
         </div>
         <div class="col-md-12">
            <TCheckboxGroup label="Kích hoạt" v-model="formData.active" :options="['Đã kích hoạt']" />
         </div>
      </div>
    </TModal>

    <!-- Modal Delete Confirmation -->
    <TModal v-model="deleteModalVisible" title="Xác nhận xóa" @ok="handleDelete" variant="danger">
       <p class="text-danger fw-bold">Bạn có chắc chắn muốn xóa đối tượng này? Thao tác này không thể hoàn tác.</p>
    </TModal>

    <!-- Toast Notifications -->
    <TToast v-model="toastVisible" :title="toastTitle" :variant="toastVariant">
       {{ toastMessage }}
    </TToast>
  </MainLayout>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import MainLayout from '@/layouts/MainLayout.vue'

// (Nếu có backend, bạn sẽ dùng service này)
// import { createCrudService } from '@/services/api'
// const entityService = createCrudService('employees')

// State dữ liệu
const items = ref<any[]>([
  { id: 1, code: 'TECH-001', name: 'Nguyễn Văn A', type: 'Admin', active: true },
  { id: 2, code: 'TECH-002', name: 'Trần Thị B', type: 'User', active: false },
])
const fields = [
  { key: 'code', label: 'Mã số', sortable: true },
  { key: 'name', label: 'Họ và tên', sortable: true },
  { key: 'type', label: 'Quyền hạn' },
  { key: 'actions', label: 'Thao tác', class: 'text-center' }
]

// State cho Tìm kiếm & Phân trang
const searchQuery = ref('')
const loading = ref(false)
const currentPage = ref(1)
const totalRows = ref(10)
const perPage = ref(5)

// State cho Modal Form
const modalVisible = ref(false)
const deleteModalVisible = ref(false)
const isEditMode = ref(false)
const selectedItem = ref<any>(null)
const formData = reactive({
  code: '',
  name: '',
  type: 'User',
  note: '',
  active: []
})
const typeOptions = ['Admin', 'User', 'Guest']

// State cho Toast
const toastVisible = ref(false)
const toastMessage = ref('')
const toastTitle = ref('Thông báo')
const toastVariant = ref('success')

// Logic
const showToast = (msg: string, variant = 'success') => {
  toastMessage.value = msg
  toastVariant.value = variant
  toastVisible.value = true
  setTimeout(() => toastVisible.value = false, 3000)
}

const openAddModal = () => {
  isEditMode.value = false
  Object.assign(formData, { code: '', name: '', type: 'User', note: '', active: [] })
  modalVisible.value = true
}

const editItem = (item: any) => {
  isEditMode.value = true
  selectedItem.value = item
  Object.assign(formData, { ...item })
  modalVisible.value = true
}

const handleSave = () => {
  if(isEditMode.value) {
    showToast('Cập nhật thành công!')
  } else {
    showToast('Thêm mới thành công!')
  }
}

const confirmDelete = (item: any) => {
  selectedItem.value = item
  deleteModalVisible.value = true
}

const handleDelete = () => {
  showToast('Đã xóa dữ liệu!', 'danger')
}

const handleSearch = () => {
  loading.value = true
  setTimeout(() => loading.value = false, 800)
}

onMounted(() => {
  // Load dữ liệu ban đầu ở đây
})
</script>
