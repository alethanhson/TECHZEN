<script setup lang="ts">
import { reactive, ref } from 'vue'
import { useRouter } from 'vue-router'
import { AuthService } from '../services/auth.service'
import { useAuth } from '../store/auth'
import { useToast } from '../store/toast'
import TInput from '../components/atoms/TInput.vue'
import TButton from '../components/atoms/TButton.vue'
import TCard from '../components/atoms/TCard.vue'

const router = useRouter()
const { setToken, setUser } = useAuth()
const toast = useToast()

const form = reactive({
  username: '',
  password: '',
})

const isLoading = ref(false)

const handleLogin = async () => {
  if (!form.username || !form.password) {
    toast.error('Vui lòng nhập đầy đủ thông tin')
    return
  }

  isLoading.value = true
  try {
    const data = await AuthService.login({
      username: form.username,
      password: form.password,
    })

    if (!data || !data.access_token) {
      console.warn('[Login Phase] API returned success but access_token is missing.', data)
      throw new Error('Đăng nhập thất bại: Token missing')
    }

    setToken(data.access_token)
    
    // Gắn đúng user trả về từ backend, lấy role.name ra cho phẳng hoặc để yên
    if (data.user) {
      setUser({
        ...data.user,
        role: data.user.role?.name || 'User'
      } as unknown)
    } else {
      // Fallback
      setUser({
        id: 1,
        username: form.username,
        email: `${form.username}@techzen.com`,
        role: 'user',
        is_superuser: false,
      } as unknown)
    }

    router.push('/')
  } catch (err) {
    console.log(err);
    // Error is already handled by api.ts toast
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div class="login-page bg-modern-gradient min-vh-100 d-flex align-items-center justify-content-center p-3">
    <div class="login-container w-100" style="max-width: 440px">
      <TCard class="login-card animate-slide-up border-0 shadow-2xl glass-effect">
        <div class="text-center mb-5 mt-3">
          <div class="brand-icon-wrapper mx-auto mb-3 shadow-lg">
            <i class="bi bi-rocket-takeoff-fill"></i>
          </div>
          <h2 class="fw-bold mb-1">Chào mừng quay lại</h2>
          <p class="text-muted small">Vui lòng đăng nhập để tiếp tục bài thi</p>
        </div>

        <form @submit.prevent="handleLogin" class="d-flex flex-column gap-2">
          <TInput
            v-model="form.username"
            label="Tên đăng nhập"
            placeholder="admin"
            class="mb-3"
            :disabled="isLoading"
          />
          <TInput
            v-model="form.password"
            label="Mật khẩu"
            type="password"
            placeholder="••••••••"
            class="mb-4"
            :disabled="isLoading"
          />

          <TButton
            type="submit"
            variant="primary"
            class="py-3 fw-bold w-100 mb-3"
            :disabled="isLoading"
            gradient
          >
            <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
            {{ isLoading ? 'Đang xác thực...' : 'Đăng nhập ngay' }}
          </TButton>

          <div class="text-center mt-3">
            <router-link to="/register" class="text-primary text-decoration-none small fw-semibold">
              Chưa có tài khoản? Đăng ký ngay
            </router-link>
          </div>
        </form>
      </TCard>
    </div>
  </div>
</template>

<style scoped lang="scss">
.login-page {
  background: linear-gradient(135deg, #f0f4ff 0%, #e6e9f0 100%);
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: -10%;
    right: -5%;
    width: 400px;
    height: 400px;
    background: radial-gradient(circle, rgba(46, 91, 255, 0.08) 0%, transparent 70%);
    border-radius: 50%;
  }

  &::after {
    content: '';
    position: absolute;
    bottom: -5%;
    left: -5%;
    width: 300px;
    height: 300px;
    background: radial-gradient(circle, rgba(102, 16, 242, 0.05) 0%, transparent 70%);
    border-radius: 50%;
  }
}

.login-card {
  padding: 1.5rem;
  border-radius: 24px;
}

.glass-effect {
  background: rgba(255, 255, 255, 0.8) !important;
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
}

.brand-icon-wrapper {
  width: 64px;
  height: 64px;
  background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%);
  border-radius: 18px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.8rem;
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
