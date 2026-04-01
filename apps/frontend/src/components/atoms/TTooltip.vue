<template>
  <BTooltip v-bind="$attrs" class="t-tooltip">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTooltip>
</template>

<style scoped>
.t-tooltip :deep(.tooltip-inner) {
  background-color: #1e293b;
  border-radius: 8px;
  padding: 0.5rem 1rem;
  font-weight: 500;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.t-tooltip :deep(.tooltip-arrow::before) {
  border-top-color: #1e293b;
}

.t-tooltip :deep(.tooltip.show) {
  opacity: 1;
}
</style>
