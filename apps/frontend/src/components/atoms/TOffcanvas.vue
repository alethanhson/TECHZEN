<template>
  <BOffcanvas v-bind="$attrs" class="t-offcanvas">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BOffcanvas>
</template>

<style scoped lang="scss">
.t-offcanvas :deep(.offcanvas-header) {
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  background-color: #f8fafc;
  padding: 1.5rem 1.75rem;
}

.t-offcanvas :deep(.offcanvas-title) {
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #1a202c;
}

.t-offcanvas :deep(.offcanvas-body) {
  padding: 1.75rem;
  color: #4a5568;
  line-height: 1.6;
}
</style>
