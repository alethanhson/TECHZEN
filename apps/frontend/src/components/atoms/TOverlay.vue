<template>
  <BOverlay v-bind="$attrs" class="t-overlay">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BOverlay>
</template>

<style scoped lang="scss">
.t-overlay :deep(.b-overlay) {
  border-radius: inherit;
  backdrop-filter: blur(12px);
  background: rgba(255, 255, 255, 0.6) !important;
  transition: all 0.3s ease;
}

.t-overlay :deep(.b-overlay .spinner-border) {
  width: 3.5rem;
  height: 3.5rem;
  color: #2E5BFF;
  border-width: 0.25em;
}
</style>
