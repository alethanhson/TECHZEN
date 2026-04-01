<template>
  <BBreadcrumbItem v-bind="$attrs" class="t-breadcrumb-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BBreadcrumbItem>
</template>

<style scoped lang="scss">
.t-breadcrumb-item :deep(.active) {
  color: #4a5568 !important;
  font-weight: 600;
}

.t-breadcrumb-item :deep(a) {
  color: #2E5BFF;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.2s ease;

  &:hover {
    color: #1e40af;
    opacity: 0.8;
  }
}
</style>
