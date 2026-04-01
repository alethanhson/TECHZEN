<template>
  <BPagination v-bind="$attrs" class="t-pagination">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BPagination>
</template>

<style scoped>
.t-pagination :deep(.page-link) {
  border: none;
  border-radius: 8px;
  margin: 0 4px;
  font-weight: 600;
  color: #64748b;
  width: 38px;
  height: 38px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s;
  background-color: #f8fafc;
}

.t-pagination :deep(.page-link:hover) {
  background-color: #f1f5f9;
  color: #1e293b;
  transform: translateY(-1px);
}

.t-pagination :deep(.page-item.active .page-link) {
  background-color: #3b82f6;
  color: #ffffff;
  box-shadow: 0 4px 6px -1px rgba(59, 130, 246, 0.4);
}

.t-pagination :deep(.page-item.disabled .page-link) {
  opacity: 0.5;
  background-color: transparent;
}
</style>
