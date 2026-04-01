<template>
  <AdminLayout>
    <div class="d-flex justify-content-between align-items-center mb-4 pb-2">
      <div class="d-flex align-items-center gap-2">
        <h2 class="fw-bold mb-0">Quản Lý Người Dùng</h2>
        <!-- POPUP (Popover) Trigger -->
        <TButton id="info-popover-target" variant="link" class="text-muted p-0 ms-1 me-2" style="font-size: 1.2rem;">
          <i class="bi bi-info-circle-fill"></i>
        </TButton>
        <TPopover target="info-popover-target" title="Quản Lý Người Dùng" triggers="hover" placement="right">
          Đây là trang danh sách người dùng trên hệ thống. Bạn có thể thêm, chỉnh sửa hoặc kiểm tra các trạng thái hoạt động mới nhất của họ.
        </TPopover>
      </div>
      
      <TButton variant="primary" class="shadow-sm" @click="showAddUserModal" gradient>
        <i class="bi bi-person-plus-fill me-2"></i> Thêm Người Dùng
      </TButton>
    </div>

    <!-- TABLE Component -->
    <TCard class="border-0 shadow-sm ps-0 pe-0">
      <template #header>
        <div class="d-flex justify-content-between align-items-center">
          <h6 class="fw-bold mb-0">Danh Sách ({{ users.length }} thành viên)</h6>
        </div>
      </template>
      
      <TTable :items="paginatedUsers" :fields="userFields" hover class="mb-0 border-0 admin-table" v-model:busy="isLoading">
        <template #table-busy>
          <div class="text-center text-primary my-5">
            <TSpinner class="align-middle" />
            <strong class="ms-2">Đang tải dữ liệu...</strong>
          </div>
        </template>
        <template #cell(user)="{ item }">
          <div class="d-flex align-items-center gap-3">
            <TAvatar :text="item.name.charAt(0)" :variant="item.color" size="sm" rounded="circle" />
            <div>
              <p class="mb-0 fw-semibold text-dark">{{ item.name }}</p>
              <p class="mb-0 text-muted extra-small">{{ item.email }}</p>
            </div>
          </div>
        </template>
        <template #cell(role)="{ item }">
          <span class="text-muted small fw-medium">{{ item.role }}</span>
        </template>
        <template #cell(status)="{ item }">
          <TBadge :variant="item.isActive ? 'success' : 'secondary'" pill class="px-2">
            {{ item.isActive ? 'Hoạt động' : 'Tạm khóa' }}
          </TBadge>
        </template>
        <template #cell(action)="{ item }">
          <div class="d-flex justify-content-end gap-2">
            <TButton variant="light" size="sm" class="btn-icon">
              <i class="bi bi-pencil"></i>
            </TButton>
            <TButton variant="light" size="sm" class="btn-icon text-danger" @click="confirmDelete(item)">
              <i class="bi bi-trash"></i>
            </TButton>
          </div>
        </template>
      </TTable>
      
      <div class="d-flex justify-content-end align-items-center p-3 border-top">
        <span class="text-muted small me-3">Hiển thị {{ paginatedUsers.length }} / {{ totalRows }}</span>
        <TPagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          class="mb-0"
        />
      </div>
    </TCard>

    <!-- MODAL Component -->
    <TModal v-model="isModalVisible" title="Thêm Người Dùng" size="md" @ok="handleSaveUser" header-bg-variant="primary" header-text-variant="white">
      <div class="d-flex flex-column gap-3">
        <TFormGroup>
          <TInput label="Họ và Tên" v-model="newUserForm.name" placeholder="Nguyễn Văn A" required />
        </TFormGroup>
        <TFormGroup>
          <TInput label="Email" v-model="newUserForm.email" type="email" placeholder="email@gmail.com" required />
        </TFormGroup>
        <TFormGroup>
          <label class="form-label text-dark fw-semibold small mb-2">Vai trò</label>
          <select class="form-select form-select-sm" v-model="newUserForm.role">
            <option value="Admin">Admin</option>
            <option value="User">User</option>
            <option value="Premium">Premium</option>
          </select>
        </TFormGroup>
      </div>
    </TModal>

    <!-- TOAST Component -->
    <div class="position-fixed bottom-0 end-0 p-4" style="z-index: 1060">
      <TToast v-model="toast.visible" :title="toast.title" :variant="toast.variant">
        {{ toast.message }}
      </TToast>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref, reactive, computed, onMounted } from 'vue'
import AdminLayout from '@/layouts/AdminLayout.vue'
import { createCrudService } from '@/services/api'

// --- API Service ---
const userApi = createCrudService<any>('users')

// --- Data State ---
const users = ref<any[]>([])
const isLoading = ref(false)

// --- Pagination State ---
const currentPage = ref(1)
const perPage = ref(5)
const totalRows = computed(() => users.value.length)

// Client-side pagination logic
const paginatedUsers = computed(() => {
  const start = (currentPage.value - 1) * perPage.value
  const end = start + perPage.value
  return users.value.slice(start, end)
})

const userFields = [
  { key: 'user', label: 'Thành viên' },
  { key: 'role', label: 'Vai trò' },
  { key: 'status', label: 'Trạng thái' },
  { key: 'action', label: 'Thao tác', class: 'text-end' },
]

// --- Initialization ---
const loadUsers = async () => {
  isLoading.value = true
  try {
    const data = await userApi.getAll()
    if (data && Array.isArray(data)) {
      const colors = ['primary', 'info', 'warning', 'success', 'danger', 'secondary']
      users.value = data.map((u: any) => ({
        ...u,
        name: u.name || u.username || 'Unknown',
        role: u.role?.name || u.role || 'User',
        isActive: u.is_active !== undefined ? u.is_active : (u.isActive !== undefined ? u.isActive : true),
        color: u.color || colors[Math.floor(Math.random() * colors.length)],
      }))
    } else {
      users.value = []
    }
  } catch (error) {
    users.value = []
  } finally {
    isLoading.value = false
  }
}


onMounted(() => {
  loadUsers()
})

// --- Modal & Form State ---
const isModalVisible = ref(false)
const newUserForm = reactive({ name: '', email: '', role: 'User' })

const showAddUserModal = () => {
  newUserForm.name = ''
  newUserForm.email = ''
  newUserForm.role = 'User'
  isModalVisible.value = true
}

const handleSaveUser = async () => {
  if (!newUserForm.name || !newUserForm.email) {
    showToast('Lỗi', 'Vui lòng nhập đầy đủ', 'danger')
    return
  }

  try {
    isLoading.value = true
    await userApi.create({
      name: newUserForm.name,
      email: newUserForm.email,
      role: newUserForm.role,
      isActive: true
    })
    showToast('Thành công!', `Đã thêm tài khoản "${newUserForm.name}"`, 'success')
    loadUsers()
  } catch (err: any) {
    showToast('Lỗi', 'Thêm tài khoản thất bại', 'danger')
  } finally {
    isModalVisible.value = false
  }
}

const confirmDelete = async (item: any) => {
  try {
    isLoading.value = true
    await userApi.delete(item.id)
    showToast('Đã xóa', `Tài khoản ${item.name} đã được dọn dẹp khỏi CSDL`, 'success')
    loadUsers()
  } catch(err) {
    showToast('Lỗi', 'Không thể xóa tài khoản', 'danger')
  } finally {
    isLoading.value = false
  }
}

// --- Toast State ---
const toast = reactive({
  visible: false,
  title: '',
  message: '',
  variant: 'success'
})

const showToast = (title: string, message: string, variant = 'success') => {
  toast.title = title
  toast.message = message
  toast.variant = variant
  toast.visible = true
  setTimeout(() => { toast.visible = false }, 4000)
}
</script>

<style scoped lang="scss">
.extra-small {
  font-size: 0.75rem;
}

.btn-icon {
  width: 32px;
  height: 32px;
  padding: 0;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  color: #6c757d;
  &:hover {
    background-color: #e9ecef;
    color: #212529;
  }
}

.admin-table {
  :deep(th) {
    font-size: 0.85rem;
    text-transform: uppercase;
    color: #6c757d;
    font-weight: 600;
    border-bottom-width: 1px;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
  }
  
  :deep(td) {
    padding-top: 1rem;
    padding-bottom: 1rem;
    vertical-align: middle;
  }
}
</style>
