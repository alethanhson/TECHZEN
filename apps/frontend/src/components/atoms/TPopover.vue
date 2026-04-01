<template>
  <BPopover v-bind="$attrs" class="t-popover">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BPopover>
</template>

<style scoped lang="scss">
.t-popover :deep(.popover) {
  border-radius: 18px;
  border: 1px solid rgba(0, 0, 0, 0.03);
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.15);
  background-color: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(8px);
}

.t-popover :deep(.popover-header) {
  background-color: #f8fafc;
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  font-weight: 700;
  color: #1a202c;
  padding: 1.125rem 1.5rem;
  border-radius: 18px 18px 0 0;
}

.t-popover :deep(.popover-body) {
  color: #4a5568;
  padding: 1.5rem;
  line-height: 1.6;
  font-size: 0.9375rem;
}

.t-popover :deep(.bs-popover-auto[data-popper-placement^=top] > .popover-arrow::after),
.t-popover :deep(.bs-popover-top > .popover-arrow::after) {
  border-top-color: white;
}
</style>
