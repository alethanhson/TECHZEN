<template>
  <BBreadcrumbItem v-bind="$attrs" class="t-breadcrumb-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BBreadcrumbItem>
</template>

<style scoped>
.t-breadcrumb-item :deep(.active) {
  color: #64748b;
  font-weight: 500;
}
</style>
