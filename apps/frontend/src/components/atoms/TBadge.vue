<template>
  <BBadge
    v-bind="$attrs"
    :variant="variant"
    :pill="pill"
    class="t-badge"
    :class="[`t-badge--${variant}`, { 't-badge--pill': pill }]"
  >
    <slot />
  </BBadge>
</template>

<script setup lang="ts">
import type { ColorVariant } from 'bootstrap-vue-next'

interface Props {
  variant?: ColorVariant | null
  pill?: boolean
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  pill: false
})
</script>

<style scoped lang="scss">
.t-badge {
  padding: 0.5em 0.85em;
  font-weight: 600;
  font-size: 0.75rem;
  letter-spacing: 0.025em;
  border-radius: 6px;
  
  &--pill {
    border-radius: 50rem;
    padding-left: 1em;
    padding-right: 1em;
  }

  // Soft color mapping
  &.bg-primary {
    background-color: rgba(46, 91, 255, 0.1) !important;
    color: #2E5BFF !important;
  }

  &.bg-success {
    background-color: rgba(0, 201, 167, 0.1) !important;
    color: #008973 !important;
  }

  &.bg-danger {
    background-color: rgba(239, 68, 68, 0.1) !important;
    color: #b91c1c !important;
  }
}
</style>
