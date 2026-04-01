<script setup lang="ts">
import { RouterView } from 'vue-router'
import { useToast } from './store/toast'

const { state: toastState } = useToast()
</script>

<template>
  <!-- Global Toasts (Bulletproof & Universal) -->
  <div class="toast-container position-fixed top-0 end-0 p-3" style="z-index: 99999">
    <div
      v-for="toast in toastState.toasts"
      :key="toast.id"
      class="toast show mb-2 animate-fade-in shadow-lg border-0"
      :class="{ 'visible': toast.visible }"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
      style="min-width: 300px; border-radius: 16px; overflow: hidden; display: block;"
    >
      <div class="toast-header border-0 pb-0" :class="`text-${toast.variant}`">
        <i class="bi me-2" :class="toast.variant === 'danger' ? 'bi-exclamation-circle-fill' : 'bi-check-circle-fill'"></i>
        <strong class="me-auto">{{ toast.title }}</strong>
        <button type="button" class="btn-close" @click="toast.visible = false"></button>
      </div>
      <div class="toast-body pt-2 pb-3 fw-medium">
        {{ toast.body }}
      </div>
      <div class="toast-progress" :class="`bg-${toast.variant}`"></div>
    </div>
  </div>

  <RouterView />
</template>

<style lang="scss">
.animate-fade-in {
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateX(50px); }
  to { opacity: 1; transform: translateX(0); }
}

.toast {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.toast-progress {
  height: 3px;
  width: 100%;
  animation: progress 5s linear forwards;
}

@keyframes progress {
  from { width: 100%; }
  to { width: 0%; }
}
</style>
