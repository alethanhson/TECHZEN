<template>
  <BBreadcrumb v-bind="$attrs" class="t-breadcrumb">
    <slot />
  </BBreadcrumb>
</template>

<style scoped>
.t-breadcrumb {
  --bs-breadcrumb-padding-x: 1rem;
  --bs-breadcrumb-padding-y: 0.75rem;
  --bs-breadcrumb-bg: #f8fafc;
  --bs-breadcrumb-item-padding-x: 0.75rem;
  --bs-breadcrumb-divider-color: #94a3b8;
  
  border-radius: 12px;
  background-color: var(--bs-breadcrumb-bg);
}
.t-breadcrumb :deep(.breadcrumb-item + .breadcrumb-item::before) {
  content: var(--bs-breadcrumb-divider, "/");
  font-weight: 300;
}
.t-breadcrumb :deep(.breadcrumb-item a) {
  text-decoration: none;
  font-weight: 600;
  color: #3b82f6;
  transition: color 0.2s;
}
.t-breadcrumb :deep(.breadcrumb-item a:hover) {
  color: #1d4ed8;
}
</style>
