<template>
  <BTooltip v-bind="$attrs" class="t-tooltip">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTooltip>
</template>

<style scoped lang="scss">
.t-tooltip :deep(.tooltip-inner) {
  background-color: #1a202c;
  border-radius: 10px;
  padding: 0.625rem 1rem;
  font-weight: 600;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
  font-size: 0.8125rem;
  letter-spacing: 0.01em;
}

.t-tooltip :deep(.tooltip-arrow::before) {
  border-top-color: #1a202c;
}

.t-tooltip :deep(.tooltip.show) {
  opacity: 1;
}
</style>
