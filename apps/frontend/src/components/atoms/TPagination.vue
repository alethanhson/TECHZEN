<template>
  <BPagination v-bind="$attrs" class="t-pagination">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BPagination>
</template>

<style scoped lang="scss">
.t-pagination :deep(.page-link) {
  border: none;
  border-radius: 10px;
  margin: 0 4px;
  font-weight: 600;
  color: #718096;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  background-color: #f8fafc;
  font-size: 0.875rem;

  &:hover {
    background-color: #edf2f7;
    color: #2E5BFF;
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  }
}

.t-pagination :deep(.page-item.active .page-link) {
  background: linear-gradient(135deg, #2E5BFF 0%, #6610f2 100%) !important;
  color: #ffffff;
  box-shadow: 0 8px 16px rgba(46, 91, 255, 0.25);
}

.t-pagination :deep(.page-item.disabled .page-link) {
  opacity: 0.4;
  background-color: transparent;
  transform: none;
}
</style>
