<template>
  <MainLayout>
    <div class="text-center py-5">
      <h1 class="fw-bold mb-3">🚀 TechZen Test System</h1>
      <p class="text-muted mb-4">Hệ thống quản lý - Bài thi thực hành</p>
      <div class="d-flex justify-content-center gap-3">
        <RouterLink to="/products" class="btn btn-primary btn-lg">
          <i class="bi bi-box-seam me-2"></i>Quản lý Sản phẩm
        </RouterLink>
      </div>
    </div>
  </MainLayout>
</template>

<script setup lang="ts">
import { RouterLink } from 'vue-router'
import MainLayout from '@/layouts/MainLayout.vue'
</script>
