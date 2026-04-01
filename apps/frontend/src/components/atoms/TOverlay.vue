<template>
  <BOverlay v-bind="$attrs" class="t-overlay">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BOverlay>
</template>

<style scoped>
.t-overlay :deep(.b-overlay) {
  border-radius: inherit;
  backdrop-filter: blur(4px);
  background: rgba(255, 255, 255, 0.4) !important;
}

.t-overlay :deep(.b-overlay .spinner-border) {
  width: 3rem;
  height: 3rem;
  color: #3b82f6;
}
</style>
