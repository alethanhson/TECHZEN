<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { AuthService } from '../services/auth.service'
import { useToast } from '../store/toast'
import TInput from '../components/atoms/TInput.vue'
import TButton from '../components/atoms/TButton.vue'
import TCard from '../components/atoms/TCard.vue'

const router = useRouter()
const toast = useToast()

const form = reactive({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
})

const isLoading = ref(false)

const handleRegister = async () => {
  if (!form.username || !form.email || !form.password) {
    toast.error('Vui lòng nhập đầy đủ thông tin')
    return
  }

  if (form.password !== form.confirmPassword) {
    toast.error('Mật khẩu xác nhận không khớp')
    return
  }

  isLoading.value = true
  try {
    await AuthService.register({
      username: form.username,
      email: form.email,
      password: form.password,
    })

    router.push('/login')
  } catch (err: unknown) {
    console.log(err);
    // Error already handled by api.ts
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="register-page bg-modern-gradient min-vh-100 d-flex align-items-center justify-content-center p-3">
    <div class="register-container w-100" style="max-width: 480px">
      <TCard class="register-card animate-slide-up border-0 shadow-2xl glass-effect">
        <div class="text-center mb-5 mt-2">
          <div class="brand-icon-wrapper mx-auto mb-3 shadow-lg">
            <i class="bi bi-person-plus-fill"></i>
          </div>
          <h2 class="fw-bold mb-1">Tạo tài khoản mới</h2>
          <p class="text-muted small">Khởi đầu hành trình chinh phục công nghệ</p>
        </div>

        <form @submit.prevent="handleRegister" class="d-flex flex-column gap-1">
          <TInput
            v-model="form.username"
            label="Tên người dùng"
            placeholder="john_doe"
            class="mb-3"
            :disabled="isLoading"
          />
          <TInput
            v-model="form.email"
            label="Email"
            type="email"
            placeholder="john@example.com"
            class="mb-3"
            :disabled="isLoading"
          />
          <div class="row g-3 mb-4">
            <div class="col-md-6">
              <TInput
                v-model="form.password"
                label="Mật khẩu"
                type="password"
                placeholder="••••••••"
                :disabled="isLoading"
              />
            </div>
            <div class="col-md-6">
              <TInput
                v-model="form.confirmPassword"
                label="Xác nhận"
                type="password"
                placeholder="••••••••"
                :disabled="isLoading"
              />
            </div>
          </div>

          <TButton
            type="submit"
            variant="primary"
            class="py-3 fw-bold w-100 mb-3"
            :disabled="isLoading"
            gradient
          >
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
            {{ isLoading ? 'Đang tạo tài khoản...' : 'Đăng ký ngay' }}
          </TButton>

          <div class="text-center mt-2">
            <router-link to="/login" class="text-primary text-decoration-none small fw-semibold">
              Đã có tài khoản? Đăng nhập tại đây
            </router-link>
          </div>
        </form>
      </TCard>
    </div>
  </div>
</template>

<style scoped lang="scss">
.register-page {
  background: linear-gradient(135deg, #e6e9f0 0%, #f0f4ff 100%);
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: -10%;
    left: -5%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(102, 16, 242, 0.06) 0%, transparent 70%);
    border-radius: 50%;
  }

  &::after {
    content: '';
    position: absolute;
    bottom: -5%;
    right: -5%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(46, 91, 255, 0.05) 0%, transparent 70%);
    border-radius: 50%;
  }
}

.register-card {
  padding: 1.5rem;
  border-radius: 24px;
}

.glass-effect {
  background: rgba(255, 255, 255, 0.8) !important;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
}

.brand-icon-wrapper {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #6610f2 0%, #2E5BFF 100%);
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.6rem;
}

.animate-slide-up {
  animation: slideUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes slideUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.shadow-2xl {
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.12);
}
</style>
