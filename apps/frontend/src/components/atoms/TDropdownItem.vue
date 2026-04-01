<template>
  <BDropdownItem v-bind="$attrs" class="t-dropdown-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BDropdownItem>
</template>

<style scoped>
.t-dropdown-item :deep(.dropdown-item) {
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: 500;
  color: #334155;
  transition: all 0.2s;
}

.t-dropdown-item :deep(.dropdown-item:hover) {
  background-color: #f1f5f9;
  color: #1e293b;
}

.t-dropdown-item :deep(.dropdown-item:active) {
  background-color: #e2e8f0;
}
</style>
