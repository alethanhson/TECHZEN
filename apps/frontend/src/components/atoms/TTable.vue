<template>
  <div class="t-table-container">
    <BTable v-bind="$attrs" class="t-table" :responsive="responsive">
      <template v-for="(_, name) in $slots" #[name]="slotData">
        <slot :name="name" v-bind="slotData || {}" />
      </template>
    </BTable>
  </div>
</template>

<script setup lang="ts">
import type { Breakpoint } from 'bootstrap-vue-next'

withDefaults(defineProps<{
  responsive?: boolean | Breakpoint
}>(), {
  responsive: true
})
</script>

<style scoped lang="scss">
.t-table-container {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(0, 0, 0, 0.03);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  background: white;
}

.t-table {
  margin-bottom: 0;
  font-size: 0.9375rem;
  border-collapse: separate;
  border-spacing: 0;

  :deep(thead th) {
    background-color: #f8fafc;
    color: #4a5568;
    font-weight: 700;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.05em;
    padding: 1.25rem 1rem;
    border-bottom: 2px solid #edf2f7;
    white-space: nowrap;
  }

  :deep(tbody td) {
    padding: 1.25rem 1rem;
    color: #2d3748;
    border-bottom: 1px solid #edf2f7;
    vertical-align: middle;
    transition: background-color 0.2s ease;
  }

  :deep(tbody tr:last-child td) {
    border-bottom: none;
  }

  :deep(tbody tr:hover) {
    background-color: #f8fafc;
    cursor: default;
  }

  // Stripe effect override
  &.table-striped > tbody > tr:nth-of-type(odd) > * {
    --bs-table-accent-bg: #fdfdfd;
  }
}
</style>
