<template>
  <BAlert
    v-bind="$attrs"
    :variant="variant || 'info'"
    :show="show || false"
    class="t-alert"
    fade
  >
    <div class="d-flex align-items-center">
      <div v-if="$slots.icon" class="me-3">
        <slot name="icon" />
      </div>
      <div>
        <slot />
      </div>
    </div>
  </BAlert>
</template>

<script setup lang="ts">
import type { BaseAlertProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseAlertProps {
  variant?: string
  show?: boolean | number
}

defineProps<Props>()
</script>

<style scoped>
.t-alert {
  border: none;
  border-radius: 12px;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
}

.t-alert-success {
  background-color: #f0fdf4;
  color: #166534;
  border-left: 5px solid #16a34a;
}

.t-alert-danger {
  background-color: #fef2f2;
  color: #991b1b;
  border-left: 5px solid #dc2626;
}

.t-alert-warning {
  background-color: #fffbeb;
  color: #92400e;
  border-left: 5px solid #d97706;
}

.t-alert-info {
  background-color: #eff6ff;
  color: #1e40af;
  border-left: 5px solid #2563eb;
}
</style>
