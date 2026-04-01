<template>
  <BNavbar v-bind="$attrs" class="t-navbar shadow-sm">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BNavbar>
</template>

<style scoped lang="scss">
.t-navbar {
  border-bottom: 1px solid rgba(0, 0, 0, 0.03);
  background-color: rgba(255, 255, 255, 0.8) !important;
  backdrop-filter: blur(16px);
  padding: 0.875rem 1.75rem;
  transition: all 0.3s ease;
}

.t-navbar :deep(.navbar-brand) {
  font-weight: 700;
  letter-spacing: -0.01em;
  color: #1a202c;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.t-navbar :deep(.nav-link) {
  font-weight: 600;
  color: #4a5568;
  padding: 0.5rem 1.25rem;
  border-radius: 10px;
  transition: all 0.2s ease;
  font-size: 0.9375rem;
}

.t-navbar :deep(.nav-link:hover) {
  background-color: rgba(46, 91, 255, 0.04);
  color: #2E5BFF;
}

.t-navbar :deep(.nav-link.active) {
  color: #2E5BFF;
  background-color: rgba(46, 91, 255, 0.08);
}
</style>
