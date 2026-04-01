<template>
  <div class="t-spinner-wrapper d-inline-flex align-items-center" :class="{ 'flex-column text-center': label }">
    <BSpinner
      v-bind="$attrs"
      :variant="variant"
      :type="type"
      :small="small"
      class="t-spinner"
    />
    <span v-if="label" :class="labelClass">{{ label }}</span>
  </div>
</template>

<script setup lang="ts">
import type { ColorVariant } from 'bootstrap-vue-next'

interface Props {
  variant?: ColorVariant | null
  type?: 'border' | 'grow'
  small?: boolean
  label?: string
  labelClass?: string
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  type: 'border',
  small: false,
  labelClass: 't-spinner-label mt-2 d-block text-muted small'
})
</script>

<style scoped lang="scss">
.t-spinner {
  border-width: 0.2em;
  
  &.spinner-border-sm {
    border-width: 0.15em;
  }
}

.t-spinner-label {
  font-weight: 600;
  letter-spacing: 0.025em;
  color: #718096;
}
</style>
