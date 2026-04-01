<template>
  <BProgress v-bind="$attrs" class="t-progress">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BProgress>
</template>

<style scoped lang="scss">
.t-progress {
  height: 0.625rem;
  border-radius: 9999px;
  background-color: #edf2f7;
  overflow: hidden;
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.04);
}

.t-progress :deep(.progress-bar) {
  border-radius: 9999px;
  transition: width 0.8s cubic-bezier(0.65, 0, 0.35, 1);
  
  &.bg-primary {
    background: linear-gradient(90deg, #2E5BFF 0%, #6610f2 100%) !important;
  }
}
</style>
