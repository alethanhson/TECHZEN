<template>
  <BProgress v-bind="$attrs" class="t-progress">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BProgress>
</template>

<style scoped>
.t-progress {
  height: 0.75rem;
  border-radius: 9999px;
  background-color: #f1f5f9;
  overflow: hidden;
  box-shadow: inset 0 2px 4px 0 rgba(0, 0, 0, 0.06);
}

.t-progress :deep(.progress-bar) {
  border-radius: 9999px;
  transition: width 0.6s cubic-bezier(0.4, 0, 0.2, 1);
}
</style>
