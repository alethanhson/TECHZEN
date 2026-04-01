<template>
  <AdminLayout>
    <!-- Page Header -->
    <div class="mb-4">
      <div class="d-flex align-items-center gap-2 mb-1">
        <h2 class="fw-bold mb-0 text-dark">Quản Lý Sản Phẩm</h2>
        <TButton
          id="product-popover-target"
          variant="link"
          class="text-muted p-0 ms-1"
          style="font-size: 1.1rem"
        >
          <i class="bi bi-info-circle-fill"></i>
        </TButton>
        <TPopover
          target="product-popover-target"
          title="Kho Sản Phẩm"
          triggers="hover"
          placement="right"
        >
          Trang chứa danh sách sản phẩm. Dữ liệu được Search và Paginate bằng Server-Side trực tiếp
          trên Database.
        </TPopover>
      </div>
      <p class="text-muted small">
        Quản lý kho hàng, theo dõi giá bán và tình trạng kinh doanh của tất cả sản phẩm.
      </p>
    </div>

    <!-- Empty State (Chỉ hiện khi chưa có bất kỳ Data nào trong kho) -->
    <div
      v-if="!loading && isDatabaseEmpty"
      class="text-center py-5 my-5 bg-white rounded-4 shadow-sm border-0"
    >
      <div class="mb-4 text-muted">
        <i class="bi bi-box-seam" style="font-size: 4rem; opacity: 0.2"></i>
      </div>
      <h4 class="fw-bold text-dark mb-2">Chưa có sản phẩm nào</h4>
      <p class="text-muted mb-4 mx-auto" style="max-width: 400px">
        Cửa hàng của bạn hiện đang trống. Hãy bắt đầu bằng việc thêm sản phẩm đầu tiên để khách hàng
        có thể mua sắm.
      </p>
      <TButton
        variant="primary"
        to="/products/create"
        class="px-4 py-2 shadow-sm rounded-3"
        gradient
      >
        <i class="bi bi-plus-lg me-2"></i> Thêm Sản Phẩm Mới
      </TButton>
    </div>

    <!-- Main Card -->
    <TCard v-else class="border-0 shadow-sm rounded-4 ps-0 pe-0">
      <!-- Card Toolbar (Search & Actions) -->
      <div
        class="px-4 py-3 border-bottom d-flex flex-column flex-md-row justify-content-between align-items-md-center gap-3 bg-white"
        style="border-top-left-radius: 1rem; border-top-right-radius: 1rem"
      >
        <div>
          <h6 class="fw-bold text-dark mb-0">
            Tất cả sản phẩm <TBadge variant="light" class="text-muted ms-2">{{ totalRows }}</TBadge>
          </h6>
        </div>
        <div class="d-flex gap-2 align-items-center">
          <div class="position-relative" style="min-width: 280px">
            <i
              class="bi bi-search position-absolute top-50 start-0 translate-middle-y ms-3 text-muted"
            ></i>
            <input
              type="text"
              class="form-control form-control-sm ps-5 py-2 rounded-3 bg-light border-0"
              v-model="searchQuery"
              placeholder="Tìm kiếm theo mã, tên..."
              @keyup.enter="handleSearch"
            />
          </div>
          <TButton
            variant="primary"
            to="/products/create"
            class="shadow-sm rounded-3 py-2 px-3 d-flex align-items-center"
            gradient
            style="white-space: nowrap"
          >
            <i class="bi bi-plus-lg me-2"></i> Thêm Mới
          </TButton>
        </div>
      </div>

      <!-- Table Section -->
      <div class="table-responsive">
        <TTable
          :items="items"
          :fields="fields"
          hover
          class="mb-0 border-0 admin-table"
          v-model:busy="loading"
        >
          <template #cell(code)="{ item }">
            <span class="text-primary fw-bold">{{ item.code }}</span>
          </template>

          <template #cell(is_active)="{ item }">
            <TBadge
              :variant="item.is_active ? 'success' : 'secondary'"
              pill
              class="px-3 py-2"
              style="font-weight: 600"
            >
              <i
                class="bi"
                :class="item.is_active ? 'bi-check-circle-fill me-1' : 'bi-pause-circle-fill me-1'"
              ></i>
              {{ item.is_active ? 'Đang bán' : 'Bản nháp' }}
            </TBadge>
          </template>

          <template #cell(price)="{ item }">
            <span class="fw-semibold text-dark"
              >{{ Number(item.price).toLocaleString('vi-VN') }} đ</span
            >
          </template>

          <template #cell(tags)="{ item }">
            <div class="d-flex flex-wrap gap-1">
              <span 
                v-for="tag in item.tags" 
                :key="tag.id" 
                class="tag-pill"
              >
                {{ tag.name }}
              </span>
              <span v-if="!item.tags || item.tags.length === 0" class="text-muted extra-small italic">
                -
              </span>
            </div>
          </template>

          <template #cell(actions)="{ item }">
            <div class="d-flex justify-content-end gap-1">
              <TButton
                variant="light"
                size="sm"
                class="btn-icon"
                :to="`/products/${item.id}/edit`"
                v-b-tooltip.hover
                title="Sửa"
              >
                <i class="bi bi-pencil-square text-secondary"></i>
              </TButton>
              <TButton
                variant="light"
                size="sm"
                class="btn-icon delete-btn"
                @click="confirmDelete(item)"
                v-b-tooltip.hover
                title="Xóa"
              >
                <i class="bi bi-trash3 text-danger"></i>
              </TButton>
            </div>
          </template>

          <template #table-busy>
            <div class="text-center text-primary my-5 py-4">
              <TSpinner class="align-middle" />
              <div class="mt-2 small fw-medium text-muted">Đang tải dữ liệu...</div>
            </div>
          </template>

          <template #empty>
            <div class="text-center text-muted my-5 py-4 bg-light mx-4 rounded-4">
              <i class="bi bi-search fs-1 d-block mb-3 text-secondary opacity-50"></i>
              <h6 class="fw-bold text-dark">Không tìm thấy kết quả phù hợp</h6>
              <span class="small"
                >Rất tiếc không có sản phẩm nào khớp với "{{ searchQuery }}".</span
              >
            </div>
          </template>
        </TTable>
      </div>

      <!-- Footer Pagination -->
      <div
        v-if="items.length > 0"
        class="d-flex flex-column flex-sm-row justify-content-between align-items-center px-4 py-3 border-top bg-white"
        style="border-bottom-left-radius: 1rem; border-bottom-right-radius: 1rem"
      >
        <span class="text-muted small fw-medium mb-3 mb-sm-0">
          Hiển thị trang <strong class="text-dark">{{ currentPage }}</strong> ({{
            items.length
          }}
          mục) - Tổng số <strong class="text-dark">{{ totalRows }}</strong>
        </span>
        <TPagination
          v-model="currentPage"
          :total-rows="totalRows"
          :per-page="perPage"
          class="mb-0"
        />
      </div>
    </TCard>

    <!-- Modal Delete -->
    <TModal
      v-model="deleteModalVisible"
      title="Xác nhận xóa"
      @ok="handleDelete"
      variant="danger"
      header-bg-variant="danger"
      header-text-variant="white"
    >
      <div class="text-center py-4">
        <div class="bg-danger bg-opacity-10 d-inline-flex p-3 rounded-circle mb-3">
          <i class="bi bi-exclamation-triangle-fill text-danger" style="font-size: 2.5rem"></i>
        </div>
        <h5 class="fw-bold mb-2 text-dark">Bạn có chắc muốn xóa sản phẩm này?</h5>
        <p class="text-muted mb-0 small px-3">
          Thao tác này là vĩnh viễn và không thể khôi phục lại dữ liệu.
        </p>
      </div>
    </TModal>

    <!-- Toast -->
    <div class="position-fixed bottom-0 end-0 p-4" style="z-index: 1060">
      <TToast v-model="toast.visible" :title="toast.title" :variant="toast.variant">
        {{ toast.message }}
      </TToast>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted, watch } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import AdminLayout from '@/layouts/AdminLayout.vue'
import { createCrudService } from '@/services/api'

const route = useRoute()
const router = useRouter()

// --- Types ---
interface Product {
  id: number
  code: string
  name: string
  description: string | null
  price: number
  quantity: number
  is_active: boolean
  tags: { id: number; name: string }[]
}

// --- API Service ---
const productApi = createCrudService<Product>('products')

// --- State ---
const isDatabaseEmpty = ref(false)
const items = ref<Product[]>([])
const loading = ref(false)

// Lấy tham số search từ URL nếu có
const searchQuery = ref((route.query.q as string) || '')
const deleteModalVisible = ref(false)
const selectedId = ref<number | null>(null)

// --- Pagination State ---
const currentPage = ref(Number(route.query.page) || 1)
const perPage = ref(5)
const totalRows = ref(0) // Lấy từ API Total

const toast = reactive({
  visible: false,
  message: '',
  title: '',
  variant: 'success',
})

const fields = [
  { key: 'code', label: 'Mã SP', sortable: true },
  { key: 'name', label: 'Tên sản phẩm', sortable: true },
  { key: 'tags', label: 'Tags' },
  { key: 'price', label: 'Giá', sortable: true },
  { key: 'quantity', label: 'Tồn kho', class: 'text-center' },
  { key: 'is_active', label: 'Trạng thái' },
  { key: 'actions', label: 'Thao tác', class: 'text-end' },
]

// --- Computed ---
// --- Actions ---
const showToast = (title: string, msg: string, variant = 'success') => {
  toast.title = title
  toast.message = msg
  toast.variant = variant
  toast.visible = true
  setTimeout(() => (toast.visible = false), 3000)
}

const updateURL = () => {
  const query: any = {}
  if (searchQuery.value) query.q = searchQuery.value
  if (currentPage.value > 1) query.page = currentPage.value
  router.replace({ query }).catch(() => {})
}

const loadData = async () => {
  loading.value = true
  updateURL() // Cập nhật params lên url
  try {
    const skip = (currentPage.value - 1) * perPage.value
    const params: any = { skip, limit: perPage.value }
    if (searchQuery.value) params.q = searchQuery.value

    const data: any = await productApi.getAll(params)

    // Server-side response format `{ items: [...], total: 100 }`
    if (data && data.items) {
      items.value = data.items
      totalRows.value = data.total
      if (!searchQuery.value) isDatabaseEmpty.value = data.total === 0
    } else if (Array.isArray(data)) {
      items.value = data
      totalRows.value = data.length
      if (!searchQuery.value) isDatabaseEmpty.value = data.length === 0
    } else {
      items.value = []
      totalRows.value = 0
      if (!searchQuery.value) isDatabaseEmpty.value = true
    }
  } catch (e: unknown) {
    console.warn('API lỗi, để danh sách trống', e)
    items.value = []
    totalRows.value = 0
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  if (currentPage.value !== 1) {
    currentPage.value = 1 // Tự động kích hoạt watch -> loadData()
  } else {
    loadData() // Kích hoạt thủ công nếu đang ở trang 1
  }
}

// Theo dõi currentPage thay đổi để gọi Server lấy trang mới
watch(currentPage, (newVal, oldVal) => {
  if (newVal !== oldVal) {
    loadData()
  }
})


const confirmDelete = (item: Product) => {
  selectedId.value = item.id
  deleteModalVisible.value = true
}

const handleDelete = async () => {
  if (!selectedId.value) return
  try {
    loading.value = true
    await productApi.delete(selectedId.value)
    await loadData()
  } catch (e: any) {
    showToast('Lỗi', 'Không thể xóa sản phẩm.', 'danger')
  } finally {
    loading.value = false
    deleteModalVisible.value = false
  }
}

onMounted(loadData)
</script>

<style scoped lang="scss">
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

.delete-btn:hover {
  background-color: #fee2e2 !important;
  i {
    color: #dc3545 !important;
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

.tag-pill {
  font-size: 0.7rem;
  background: #f1f5f9;
  color: #64748b;
  padding: 2px 8px;
  border-radius: 6px;
  border: 1px solid #e2e8f0;
  font-weight: 500;
}

.extra-small {
  font-size: 0.75rem;
}

.italic {
  font-style: italic;
}
</style>
