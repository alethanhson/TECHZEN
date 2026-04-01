<template>
  <BDropdown
    v-bind="$attrs"
    :variant="variant || 'light'"
    :size="size || 'md'"
    class="t-dropdown"
  >
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BDropdown>
</template>

<script setup lang="ts">
import type { BaseDropdownProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseDropdownProps {
  variant?: string
  size?: 'sm' | 'md' | 'lg'
}

defineProps<Props>()
</script>

<style scoped>
.t-dropdown :deep(.dropdown-toggle) {
  border-radius: 8px;
  font-weight: 500;
  border: 1px solid #e2e8f0;
  transition: all 0.2s;
}

.t-dropdown :deep(.dropdown-toggle:hover) {
  background-color: #f8fafc;
  border-color: #cbd5e1;
}

.t-dropdown :deep(.dropdown-menu) {
  border-radius: 12px;
  border: 1px solid #f1f5f9;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
  padding: 0.5rem;
  margin-top: 0.5rem !important;
}
</style>
