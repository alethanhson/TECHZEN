<template>
  <AdminLayout>
    <div class="d-flex justify-content-between align-items-center mb-4 pb-2">
      <div class="d-flex align-items-center gap-2">
        <TButton variant="link" class="text-secondary p-0 me-2 fs-5" @click="goBack">
          <i class="bi bi-arrow-left"></i>
        </TButton>
        <h2 class="fw-bold mb-0">{{ isEditMode ? 'Chỉnh Sửa Sản Phẩm' : 'Thêm Sản Phẩm Mới' }}</h2>
      </div>
      <div class="d-flex gap-2">
        <TButton variant="light" class="shadow-sm fw-medium" @click="goBack">
          Hủy bỏ
        </TButton>
        <TButton variant="primary" class="shadow-sm fw-medium px-4" @click="onSubmit" gradient :disabled="loading">
          <TSpinner v-if="loading" small class="me-2" />
          {{ isEditMode ? 'Cập Nhật' : 'Lưu Sản Phẩm' }}
        </TButton>
      </div>
    </div>

    <!-- Main Form Content -->
    <div class="row g-4 pb-5">
      <!-- Left Column (Main details) -->
      <div class="col-12 col-xl-8 d-flex flex-column gap-4">
        
        <!-- Basic Info Card -->
        <TCard class="border-0 shadow-sm ps-0 pe-0">
          <template #header>
            <h6 class="fw-bold mb-0">Thông Tin Chung</h6>
          </template>
          <div class="row g-4 mt-1">
            <div class="col-md-12">
              <TFormGroup>
                <TInput 
                  label="Tên sản phẩm *" 
                  v-model="name" 
                  placeholder="Ví dụ: Áo thun nam Polo..." 
                  required 
                  :state="errors.name ? false : (name ? true : null)"
                  :feedback="errors.name"
                />
              </TFormGroup>
            </div>
            <div class="col-md-12">
              <TFormGroup>
                <TTextarea label="Mô tả chi tiết" v-model="description" rows="5" placeholder="Nhập mô tả sản phẩm của bạn..." />
              </TFormGroup>
            </div>
          </div>
        </TCard>

        <!-- Pricing & Inventory Card -->
        <TCard class="border-0 shadow-sm ps-0 pe-0">
          <template #header>
            <h6 class="fw-bold mb-0">Định Giá &amp; Tồn Kho</h6>
          </template>
          <div class="row g-4 mt-1">
            <div class="col-md-6">
              <TFormGroup>
                <TInput 
                  label="Mã SKU (Tùy chọn)" 
                  v-model="code" 
                  placeholder="VD: POLO-001" 
                  :disabled="isEditMode"
                  :state="errors.code ? false : (code ? true : null)"
                  :feedback="errors.code"
                />
              </TFormGroup>
            </div>
            <div class="col-md-6">
              <TFormGroup>
                <TInput 
                  label="Giá bán lẻ (VNĐ) *" 
                  v-model.number="price" 
                  type="number" 
                  placeholder="0"
                  :state="errors.price ? false : (price !== undefined ? true : null)"
                  :feedback="errors.price"
                />
              </TFormGroup>
            </div>
            <div class="col-md-6">
              <TFormGroup>
                <TInput 
                  label="Số lượng tồn kho *" 
                  v-model.number="quantity" 
                  type="number" 
                  placeholder="0"
                  :state="errors.quantity ? false : (quantity !== undefined ? true : null)"
                  :feedback="errors.quantity"
                />
              </TFormGroup>
            </div>
          </div>
        </TCard>
      </div>

      <!-- Right Column (Sidebar details) -->
      <div class="col-12 col-xl-4 d-flex flex-column gap-4">
        
        <!-- Status Card -->
        <TCard class="border-0 shadow-sm ps-0 pe-0">
          <template #header>
            <h6 class="fw-bold mb-0">Trạng Thái Kinh Doanh</h6>
          </template>
          <div class="mt-2">
            <TFormGroup>
              <select class="form-select form-select mb-3" v-model="status">
                <option value="active">Đang kinh doanh (Hiển thị)</option>
                <option value="inactive">Ngừng kinh doanh (Bản nháp)</option>
              </select>
            </TFormGroup>
            <div class="bg-light p-3 rounded text-muted small">
              Sản phẩm "Đang kinh doanh" sẽ xuất hiện trên trang mua sắm và có thể được tích hợp vào các đơn hàng.
            </div>
          </div>
        </TCard>

        <!-- Tags Card -->
        <TCard class="border-0 shadow-sm ps-0 pe-0">
          <template #header>
            <h6 class="fw-bold mb-0">Phân loại & Thẻ (Tags)</h6>
          </template>
          <div class="mt-2">
            <div class="d-flex gap-2 mb-3">
              <TInput 
                v-model="newTag" 
                placeholder="Thêm tag..." 
                @keypress.enter.prevent="addTag"
                class="flex-grow-1"
              />
              <TButton variant="light" @click="addTag" :disabled="!newTag.trim()">
                <i class="bi bi-plus-lg"></i>
              </TButton>
            </div>
            
            <div class="d-flex flex-wrap gap-2">
              <div v-for="(tag, index) in values.tags" :key="index" class="badge-tag d-flex align-items-center gap-2">
                <span>{{ tag }}</span>
                <i class="bi bi-x-circle-fill cursor-pointer" @click="removeTag(index)"></i>
              </div>
              <div v-if="!values.tags || values.tags?.length === 0" class="text-muted small italic w-100 text-center py-2">
                Chưa có thẻ nào được gắn.
              </div>
            </div>
          </div>
        </TCard>

      </div>
    </div>
    
    <!-- Toast -->
    <div class="position-fixed bottom-0 end-0 p-4" style="z-index: 1060">
      <TToast v-model="toast.visible" :title="toast.title" :variant="toast.variant">
        {{ toast.message }}
      </TToast>
    </div>
  </AdminLayout>
</template>

<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useForm } from 'vee-validate'
import { toTypedSchema } from '@vee-validate/zod'
import { productSchema, type ProductFormValues } from '@/schemas/product.schema'
import AdminLayout from '@/layouts/AdminLayout.vue'
import { createCrudService } from '@/services/api'

// --- Types ---
interface Product {
  id?: number
  code: string
  name: string
  description: string | null
  price: number
  quantity: number
  is_active: boolean
  tags?: { id: number; name: string }[]
}

// --- Setup ---
const route = useRoute()
const router = useRouter()
const productApi = createCrudService<Product>('products')

const isEditMode = computed(() => {
  return route.params.id !== undefined && route.params.id !== ''
})

const loading = ref(false)
const toast = ref({ visible: false, title: '', message: '', variant: 'success' })

// --- VeeValidate Setup ---
const { values, errors, defineField, handleSubmit, setValues, setFieldValue } = useForm<ProductFormValues>({
  validationSchema: toTypedSchema(productSchema),
  initialValues: {
    code: '',
    name: '',
    description: '',
    price: 0,
    quantity: 0,
    status: 'active',
    tags: []
  }
})

const [name] = defineField('name')
const [code] = defineField('code')
const [description] = defineField('description')
const [price] = defineField('price')
const [quantity] = defineField('quantity')
const [status] = defineField('status')

const newTag = ref('')

// --- Actions ---
const goBack = () => {
  router.push('/products')
}

const addTag = () => {
  const tag = newTag.value.trim()
  const currentTags = values.tags || []
  if (tag && !currentTags.includes(tag)) {
    setFieldValue('tags', [...currentTags, tag])
    newTag.value = ''
  }
}

const removeTag = (index: number) => {
  const currentTags = [...(values.tags || [])]
  currentTags.splice(index, 1)
  setFieldValue('tags', currentTags)
}

const showToast = (title: string, msg: string, variant = 'success') => {
  toast.value.title = title
  toast.value.message = msg
  toast.value.variant = variant
  toast.value.visible = true
  setTimeout(() => (toast.value.visible = false), 3500)
}

const loadProductData = async () => {
  if (!isEditMode.value) return
  
  const idStr = route.params.id as string
  const id = parseInt(idStr)
  if (isNaN(id)) return

  loading.value = true
  try {
    const data = await productApi.getById(id)
    if (data) {
      setValues({
        code: data.code || '',
        name: data.name || '',
        description: data.description || '',
        price: data.price || 0,
        quantity: data.quantity || 0,
        status: data.is_active ? 'active' : 'inactive',
        tags: data.tags?.map(t => t.name) || []
      })
    } else {
      throw new Error("Không tìm thấy dữ liệu từ API")
    }
  } catch (error) {
    showToast('Lỗi', 'Không lấy được dữ liệu sản phẩm.', 'danger')
  } finally {
    loading.value = false
  }
}

const onSubmit = handleSubmit(async (formValues) => {
  const payload = {
    code: formValues.code || `SP-${Math.floor(Math.random() * 10000)}`,
    name: formValues.name,
    description: formValues.description || null,
    price: Number(formValues.price),
    quantity: Number(formValues.quantity),
    is_active: formValues.status === 'active',
    tags: formValues.tags
  }

  loading.value = true
  try {
    if (isEditMode.value) {
      const id = parseInt(route.params.id as string)
      await productApi.update(id, payload as Product)
    } else {
      await productApi.create(payload as Product)
    }
    
    setTimeout(() => {
      router.push('/products')
    }, 1500)
  } catch(e) {
    showToast('Lỗi', 'Lưu sản phẩm thất bại.', 'danger')
  } finally {
    loading.value = false
  }
})

onMounted(() => {
  loadProductData()
})
</script>

<style scoped>
.border-dashed {
  border-style: dashed !important;
  border-width: 2px !important;
  border-color: #dee2e6 !important;
}
.badge-tag {
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  padding: 4px 10px;
  border-radius: 8px;
  font-size: 0.85rem;
  font-weight: 500;
  color: #475569;
}

.cursor-pointer {
  cursor: pointer;
}

.italic {
  font-style: italic;
}
</style>
