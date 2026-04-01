<template>
  <BPopover v-bind="$attrs" class="t-popover">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BPopover>
</template>

<style scoped>
.t-popover :deep(.popover) {
  border-radius: 16px;
  border: 1px solid #f1f5f9;
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.t-popover :deep(.popover-header) {
  background-color: #f8fafc;
  border-bottom: 1px solid #f1f5f9;
  font-weight: 800;
  color: #1e293b;
  padding: 1rem 1.25rem;
  border-radius: 16px 16px 0 0;
}

.t-popover :deep(.popover-body) {
  color: #475569;
  padding: 1.25rem;
  line-height: 1.6;
}
</style>
