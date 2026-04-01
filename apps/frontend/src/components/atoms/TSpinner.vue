<template>
  <div class="t-spinner-wrapper" :class="{ 'flex-column text-center': label }">
    <BSpinner
      v-bind="$attrs"
      :variant="variant || 'primary'"
      :type="type || 'border'"
      :small="small || false"
      class="t-spinner"
    />
    <span v-if="label" class="t-spinner-label mt-2 d-block text-muted small">{{ label }}</span>
  </div>
</template>

<script setup lang="ts">
import type { BaseSpinnerProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseSpinnerProps {
  variant?: string
  type?: 'border' | 'grow'
  small?: boolean
  label?: string
}

defineProps<Props>()
</script>

<style scoped>
.t-spinner {
  width: var(--t-spinner-size, 1.5rem);
  height: var(--t-spinner-size, 1.5rem);
}

.t-spinner-label {
  font-weight: 500;
}
</style>
