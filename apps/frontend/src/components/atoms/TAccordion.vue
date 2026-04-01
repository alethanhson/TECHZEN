<template>
  <BAccordion v-bind="$attrs" class="t-accordion">
    <slot />
  </BAccordion>
</template>

<style scoped>
.t-accordion {
  --bs-accordion-border-radius: 12px;
  --bs-accordion-inner-border-radius: 11px;
}
.t-accordion :deep(.accordion-item) {
  margin-bottom: 8px;
  border-radius: var(--bs-accordion-border-radius);
  overflow: hidden;
  border: 1px solid #edf2f7;
  box-shadow: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
}
.t-accordion :deep(.accordion-button:not(.collapsed)) {
  background-color: #f8fafc;
  color: #1e293b;
  box-shadow: none;
}
.t-accordion :deep(.accordion-button:focus) {
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}
</style>
