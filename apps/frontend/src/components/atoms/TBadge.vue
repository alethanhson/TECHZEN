<template>
  <BBadge
    v-bind="$attrs"
    :variant="variant || 'secondary'"
    :pill="pill || false"
    class="t-badge"
  >
    <slot />
  </BBadge>
</template>

<script setup lang="ts">
import type { BaseBadgeProps } from 'bootstrap-vue-next'

interface Props extends /* @vue-ignore */ BaseBadgeProps {
  variant?: string
  pill?: boolean
}

defineProps<Props>()
</script>

<style scoped>
.t-badge {
  padding: 0.5em 1em;
  font-weight: 600;
  border-radius: 4px;
}

.t-badge:not(.rounded-pill) {
  border-radius: 6px;
}
</style>
