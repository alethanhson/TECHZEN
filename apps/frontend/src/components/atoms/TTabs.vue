<template>
  <BTabs v-bind="$attrs" class="t-tabs">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTabs>
</template>

<style scoped>
.t-tabs :deep(.nav-tabs) {
  border-bottom: 2px solid #f1f5f9;
  gap: 1rem;
}

.t-tabs :deep(.nav-link) {
  border: none;
  font-weight: 600;
  color: #64748b;
  padding: 1rem 1.5rem;
  border-radius: 8px 8px 0 0;
  position: relative;
  transition: all 0.2s;
}

.t-tabs :deep(.nav-link.active) {
  background-color: transparent;
  color: #3b82f6;
}

.t-tabs :deep(.nav-link.active::after) {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 2px;
  background-color: #3b82f6;
}

.t-tabs :deep(.tab-content) {
  padding: 2rem 0;
  color: #475569;
}
</style>
