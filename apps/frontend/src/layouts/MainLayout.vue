<template>
  <div class="main-layout min-vh-100 d-flex flex-column">
    <!-- Header -->
    <TNavbar sticky="top" class="t-main-navbar">
      <div class="container d-flex justify-content-between align-items-center">
        <BNavbarBrand to="/" class="d-flex align-items-center gap-2">
          <div class="icon-box bg-modern-gradient rounded-xl shadow-sm">
            <i class="bi bi-rocket-takeoff-fill"></i>
          </div>
          <span class="brand-text">TECHZEN<span class="text-primary">.EXAM</span></span>
        </BNavbarBrand>

        <div class="d-flex gap-3 align-items-center">
          <TLink to="/" class="text-dark nav-item-link d-none d-md-block">Trang chủ</TLink>
          <TLink to="/products" class="text-dark nav-item-link d-none d-sm-block">Sản phẩm</TLink>
          <TLink v-if="authState.isAuthenticated" to="/dashboard" class="text-dark nav-item-link d-none d-sm-block">Dashboard</TLink>

          <div class="ms-2 d-flex gap-2">
            <template v-if="!authState.isAuthenticated">
              <TButton to="/login" variant="light" size="sm" class="px-3 fw-bold"
                >Đăng nhập</TButton
              >
              <TButton
                to="/register"
                variant="primary"
                size="sm"
                class="px-3 fw-bold shadow-sm"
                gradient
                >Đăng ký</TButton
              >
            </template>

            <template v-else>
              <TDropdown no-caret variant="link" class="p-0 user-dropdown">
                <template #button-content>
                  <div class="user-profile-circle shadow-sm border">
                    <span class="user-initials">{{
                      authState.user?.username?.charAt(0).toUpperCase() || 'U'
                    }}</span>
                  </div>
                </template>
                <TDropdownItem class="py-2 px-3">
                  <div class="small fw-bold">{{ authState.user?.username || 'Người dùng' }}</div>
                  <div class="extra-small text-muted">{{ authState.user?.email || '' }}</div>
                </TDropdownItem>
                <TDropdownDivider />
                <TDropdownItem @click="handleLogout" variant="danger" class="py-2 px-3 fw-medium">
                  <i class="bi bi-box-arrow-right me-2"></i> Đăng xuất
                </TDropdownItem>
              </TDropdown>
            </template>
          </div>
        </div>
      </div>
    </TNavbar>

    <!-- Main Content -->
    <main class="flex-grow-1">
      <slot />
    </main>

    <!-- Footer -->
    <footer class="footer mt-auto">
      <div class="container py-5">
        <div class="row g-4 align-items-center">
          <div class="col-md-6 text-center text-md-start">
            <h5 class="fw-bold mb-2">TECHZEN</h5>
            <p class="text-muted small mb-0">© 2026 Techzen Education - Exam Preparation System</p>
          </div>
          <!-- <div class="col-md-6 text-center text-md-end">
            <div class="d-flex justify-content-center justify-content-md-end gap-3 mb-3">
              <TLink href="#" class="text-muted small">Quy định</TLink>
              <TLink href="#" class="text-muted small">Hỗ trợ</TLink>
            </div>
          </div> -->
        </div>
      </div>
    </footer>
  </div>
</template>

<script setup lang="ts">
import { useAuth } from '../store/auth'
import { useRouter } from 'vue-router'

const { state: authState, logout: authLogout } = useAuth()
const router = useRouter()

const handleLogout = () => {
  authLogout()
  router.push('/login')
}
</script>

<style scoped lang="scss">
.main-layout {
  background-color: #f8fafc;
  font-family: 'Inter', system-ui, sans-serif;
  color: #1a202c;
  min-height: 100vh;
}

.t-main-navbar {
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  z-index: 1050;
}

.brand-text {
  font-weight: 800;
  letter-spacing: -0.05em;
  font-size: 1.25rem;
}

.icon-box {
  width: 36px;
  height: 36px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.1rem;
}

.nav-item-link {
  font-size: 0.9375rem;
  font-weight: 600;
  color: #4a5568 !important;

  &:hover {
    color: #2e5bff !important;
  }
}

.footer {
  background-color: white;
  border-top: 1px solid rgba(0, 0, 0, 0.03);
}

.rounded-xl {
  border-radius: 10px;
}

.user-profile-circle {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  transition: all 0.2s ease;

  &:hover {
    transform: scale(1.05);
    border-color: #2e5bff !important;
  }
}

.user-initials {
  font-weight: 700;
  font-size: 0.9rem;
  color: #2e5bff;
}

.extra-small {
  font-size: 0.75rem;
}

.rounded-xl {
  border-radius: 10px;
}
</style>
