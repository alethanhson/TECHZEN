<template>
  <BButton
    v-bind="$attrs"
    :variant="variant || 'primary'"
    :size="size || 'md'"
    class="t-button"
  >
    <slot />
  </BButton>
</template>

<script setup lang="ts">
import type { BaseButtonProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseButtonProps {
  variant?: string
  size?: 'sm' | 'md' | 'lg'
}

defineProps<Props>()
</script>

<style scoped>
.t-button {
  border-radius: 6px;
  font-weight: 500;
  transition: all 0.2s ease-in-out;
}

.t-button:hover {
  filter: brightness(0.95);
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.t-button:active {
  transform: translateY(1px);
}
</style>
