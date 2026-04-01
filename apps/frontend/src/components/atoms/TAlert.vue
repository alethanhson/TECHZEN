<template>
  <BAlert
    v-bind="$attrs"
    :variant="variant"
    :model-value="show"
    class="t-alert shadow-sm"
    fade
  >
    <div class="d-flex align-items-center">
      <div v-if="$slots.icon" class="me-3 t-alert__icon">
        <slot name="icon" />
      </div>
      <div class="t-alert__content">
        <slot />
      </div>
    </div>
  </BAlert>
</template>

<script setup lang="ts">
import type { ColorVariant } from 'bootstrap-vue-next'

interface Props {
  variant?: ColorVariant | null
  show?: boolean | number
}

withDefaults(defineProps<Props>(), {
  variant: 'info',
  show: true
})
</script>

<style scoped lang="scss">
.t-alert {
  border: none;
  border-radius: 12px;
  padding: 1rem 1.25rem;
  font-weight: 500;
  font-size: 0.9375rem;

  &.alert-success {
    background-color: #f0fdf9;
    color: #008973;
    border-left: 5px solid #00C9A7;
  }

  &.alert-danger {
    background-color: #fef2f2;
    color: #b91c1c;
    border-left: 5px solid #ef4444;
  }

  &.alert-warning {
    background-color: #fffbeb;
    color: #92400e;
    border-left: 5px solid #f59e0b;
  }

  &.alert-info {
    background-color: #f0f4ff;
    color: #2E5BFF;
    border-left: 5px solid #2E5BFF;
  }

  &__icon {
    font-size: 1.25rem;
    opacity: 0.9;
  }
}
</style>
