<template>
  <BDropdown
    v-bind="$attrs"
    :variant="variant"
    :size="size"
    class="t-dropdown"
  >
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BDropdown>
</template>

<script setup lang="ts">
import type { ButtonVariant } from 'bootstrap-vue-next'

interface Props {
  variant?: ButtonVariant | null
  size?: 'sm' | 'md' | 'lg'
}

withDefaults(defineProps<Props>(), {
  variant: 'light',
  size: 'md'
})
</script>

<style scoped lang="scss">
.t-dropdown :deep(.dropdown-toggle) {
  border-radius: 10px;
  font-weight: 600;
  border: 1px solid rgba(0, 0, 0, 0.05);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  padding: 0.625rem 1.25rem;
  background-color: white;
  color: #4a5568;

  &:hover {
    background-color: #f8fafc;
    border-color: #cbd5e1;
    transform: translateY(-1px);
  }

  &.btn-primary {
    background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%) !important;
    border: none;
    color: white;
  }
}

.t-dropdown :deep(.dropdown-menu) {
  border-radius: 14px;
  border: 1px solid rgba(0, 0, 0, 0.03);
  box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
  padding: 0.75rem;
  margin-top: 0.75rem !important;
  backdrop-filter: blur(8px);
  background-color: rgba(255, 255, 255, 0.95);
}
</style>
