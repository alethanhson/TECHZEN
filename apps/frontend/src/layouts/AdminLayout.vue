<template>
  <MainLayout>
    <div class="dashboard-wrapper d-flex">
      <!-- SIDEBAR -->
      <aside class="dashboard-sidebar bg-white border-end d-none d-md-flex flex-column py-4 px-3" style="width: 260px; min-height: calc(100vh - 70px);">
        <div class="mb-4 px-2">
          <small class="text-uppercase text-muted fw-bold extra-small tracking-wide">Menu Quản trị</small>
        </div>
        
        <ul class="nav flex-column gap-2 mb-auto sidebar-list">
          <li class="nav-item">
            <router-link to="/dashboard" class="nav-link d-flex align-items-center gap-3 rounded-3 px-3 py-2" active-class="active">
              <i class="bi bi-grid-1x2-fill"></i>
              <span class="fw-medium">Tổng Quan</span>
            </router-link>
          </li>
          <li class="nav-item">
            <router-link to="/products" class="nav-link d-flex align-items-center gap-3 rounded-3 px-3 py-2" active-class="active">
              <i class="bi bi-box-seam"></i>
              <span class="fw-medium">Sản Phẩm</span>
            </router-link>
          </li>
          <li class="nav-item">
            <a href="#" class="nav-link d-flex align-items-center gap-3 rounded-3 px-3 py-2">
              <i class="bi bi-people"></i>
              <span class="fw-medium">Người Dùng</span>
              <TBadge variant="primary" pill class="ms-auto">Demo</TBadge>
            </a>
          </li>
          <li class="nav-item mt-4">
            <a href="#" class="nav-link d-flex align-items-center gap-3 rounded-3 px-3 py-2 text-danger">
              <i class="bi bi-box-arrow-left"></i>
              <span class="fw-medium">Thoát</span>
            </a>
          </li>
        </ul>
      </aside>

      <!-- MAIN CONTENT (SLOT) -->
      <main class="dashboard-content flex-grow-1 p-4 p-md-5 bg-light" style="width: calc(100% - 260px);">
        <slot />
      </main>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import MainLayout from './MainLayout.vue'
</script>

<style scoped lang="scss">
.dashboard-wrapper {
  background-color: #f4f6fb;
}

.tracking-wide {
  letter-spacing: 0.05em;
}

.extra-small {
  font-size: 0.75rem;
}

/* Sidebar List Styling */
.sidebar-list {
  .nav-link {
    color: #4a5568;
    transition: all 0.2s ease;
    
    i {
      font-size: 1.1rem;
      opacity: 0.7;
    }

    &:hover {
      background-color: #f8fafc;
      color: #2e5bff;
      i { color: #2e5bff; opacity: 1; }
    }

    &.active {
      background-color: rgba(46, 91, 255, 0.1) !important;
      color: #2e5bff !important;
      i { color: #2e5bff; opacity: 1; }
    }
  }
}
</style>
