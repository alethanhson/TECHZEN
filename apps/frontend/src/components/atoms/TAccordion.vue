<template>
  <BAccordion v-bind="$attrs" class="t-accordion">
    <slot />
  </BAccordion>
</template>

<style scoped lang="scss">
.t-accordion {
  --bs-accordion-border-radius: 12px;
  --bs-accordion-inner-border-radius: 11px;
}
.t-accordion :deep(.accordion-item) {
  margin-bottom: 12px;
  border-radius: var(--bs-accordion-border-radius) !important;
  overflow: hidden;
  border: 1px solid rgba(0, 0, 0, 0.03);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  background: white;
}
.t-accordion :deep(.accordion-button) {
  font-weight: 600;
  padding: 1.25rem 1.5rem;
  transition: all 0.2s ease;
  
  &:not(.collapsed) {
    background-color: #f8fafc;
    color: #2E5BFF;
    box-shadow: none;
  }
  
  &:focus {
    box-shadow: 0 0 0 4px rgba(46, 91, 255, 0.1);
  }
}

.t-accordion :deep(.accordion-body) {
  padding: 1.5rem;
  color: #4a5568;
  line-height: 1.6;
}
</style>
