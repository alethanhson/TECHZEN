<template>
  <BDropdownItem v-bind="$attrs" class="t-dropdown-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BDropdownItem>
</template>

<style scoped lang="scss">
.t-dropdown-item :deep(.dropdown-item) {
  border-radius: 8px;
  padding: 0.625rem 1rem;
  font-weight: 500;
  color: #4a5568;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  font-size: 0.875rem;

  &:hover {
    background-color: rgba(46, 91, 255, 0.05);
    color: #2E5BFF;
    transform: translateX(4px);
  }

  &:active {
    background-color: rgba(46, 91, 255, 0.1);
    color: #2E5BFF;
  }
  
  &.text-danger {
    color: #e53e3e !important;
    &:hover {
      background-color: rgba(229, 62, 62, 0.05);
      color: #c53030 !important;
    }
  }
}
</style>
