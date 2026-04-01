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
withDefaults(defineProps<{
  responsive?: boolean | string
}>(), {
  responsive: true
})
</script>

<style scoped>
.t-table-container {
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid #f1f5f9;
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
}

.t-table {
  margin-bottom: 0;
  font-size: 14px;
}

.t-table :deep(thead th) {
  background-color: #f8fafc;
  color: #64748b;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 1rem;
  border-bottom: 2px solid #f1f5f9;
}

.t-table :deep(tbody td) {
  padding: 1rem;
  color: #334155;
  border-bottom: 1px solid #f1f5f9;
  vertical-align: middle;
}

.t-table :deep(tbody tr:last-child td) {
  border-bottom: none;
}

.t-table :deep(tbody tr:hover) {
  background-color: #f1f5f9;
  cursor: pointer;
}
</style>
