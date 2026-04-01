<template>
  <BButton
    v-bind="$attrs"
    :variant="variant || 'primary'"
    :size="size || 'md'"
    class="t-button"
    :class="{ 't-button--gradient': gradient }"
  >
    <slot />
  </BButton>
</template>

<script setup lang="ts">
import type { ButtonVariant } from 'bootstrap-vue-next'

interface Props {
  variant?: ButtonVariant | null
  size?: 'sm' | 'md' | 'lg'
  gradient?: boolean
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md',
  gradient: false
})
</script>

<style scoped lang="scss">
.t-button {
  // border-radius and shadows are handled by Bootstrap Overrides in main.scss
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  letter-spacing: 0.01em;

  // Modern Soft Gradient
  &--gradient {
    &.btn-primary {
      background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%) !important;
      border: none;
      box-shadow: 0 4px 12px rgba(46, 91, 255, 0.2);
    }
  }

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 15px rgba(0, 0, 0, 0.1);
  }

  &:active {
    transform: translateY(0);
  }
}
</style>
