<script setup lang="ts">
import type { ColorVariant } from 'bootstrap-vue-next'

defineProps<{
  modelValue?: boolean
  variant?: ColorVariant | null
  title?: string
}>()

defineEmits<{
  'update:modelValue': [value: boolean]
}>()
</script>

<template>
  <BToast
    :model-value="modelValue"
    @update:model-value="$emit('update:modelValue', !!$event)"
    :variant="variant"
    :title="title"
    v-bind="$attrs"
    class="t-toast"
    no-auto-hide
  >
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BToast>
</template>

<style scoped lang="scss">
.t-toast :deep(.toast) {
  border-radius: 16px;
  border: 1px solid rgba(0, 0, 0, 0.03);
  background-color: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(16px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
}

.t-toast :deep(.toast-header) {
  background-color: transparent;
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  padding: 0.875rem 1.25rem;
  font-weight: 700;
  color: #1a202c;
  letter-spacing: -0.01em;
}

.t-toast :deep(.toast-body) {
  padding: 1.25rem;
  color: #4a5568;
  font-size: 0.9375rem;
  line-height: 1.5;
}
</style>
