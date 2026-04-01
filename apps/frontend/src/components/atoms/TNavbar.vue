<template>
  <BNavbar v-bind="$attrs" class="t-navbar">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BNavbar>
</template>

<style scoped>
.t-navbar {
  border-bottom: 1px solid #f1f5f9;
  background-color: rgba(255, 255, 255, 0.8) !important;
  backdrop-filter: blur(12px);
  padding: 0.75rem 1.5rem;
}

.t-navbar :deep(.navbar-brand) {
  font-weight: 800;
  letter-spacing: -0.025em;
  color: #1e293b;
}

.t-navbar :deep(.nav-link) {
  font-weight: 600;
  color: #64748b;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  transition: all 0.2s;
}

.t-navbar :deep(.nav-link:hover) {
  background-color: #f1f5f9;
  color: #1e293b;
}

.t-navbar :deep(.nav-link.active) {
  color: #3b82f6;
  background-color: rgba(59, 130, 246, 0.05);
}
</style>
