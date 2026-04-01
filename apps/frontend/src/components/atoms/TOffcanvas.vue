<template>
  <BOffcanvas v-bind="$attrs" class="t-offcanvas">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BOffcanvas>
</template>

<style scoped>
.t-offcanvas :deep(.offcanvas-header) {
  border-bottom: 1px solid #f1f5f9;
  background-color: #f8fafc;
  padding: 1.5rem;
}

.t-offcanvas :deep(.offcanvas-title) {
  font-weight: 800;
  letter-spacing: -0.025em;
  color: #1e293b;
}

.t-offcanvas :deep(.offcanvas-body) {
  padding: 1.5rem;
  color: #475569;
}
</style>
