<template>
  <BBreadcrumb v-bind="$attrs" class="t-breadcrumb">
    <slot />
  </BBreadcrumb>
</template>

<style scoped lang="scss">
.t-breadcrumb {
  --bs-breadcrumb-padding-x: 1.25rem;
  --bs-breadcrumb-padding-y: 0.875rem;
  --bs-breadcrumb-bg: #f8fafc;
  --bs-breadcrumb-item-padding-x: 0.75rem;
  --bs-breadcrumb-divider-color: #cbd5e1;
  
  border-radius: 14px;
  background-color: var(--bs-breadcrumb-bg);
  border: 1px solid rgba(0, 0, 0, 0.02);
  display: inline-flex;
}

.t-breadcrumb :deep(.breadcrumb-item) {
  font-size: 0.875rem;
  font-weight: 500;
  color: #718096;

  & + .breadcrumb-item::before {
    content: var(--bs-breadcrumb-divider, "•") !important;
    font-size: 1.2rem;
    line-height: 1;
    vertical-align: middle;
    color: #cbd5e1;
  }

  a {
    text-decoration: none;
    font-weight: 600;
    color: #2E5BFF;
    transition: all 0.2s ease;
    
    &:hover {
      color: #1e40af;
      opacity: 0.8;
    }
  }

  &.active {
    color: #4a5568;
    font-weight: 600;
  }
}
</style>
