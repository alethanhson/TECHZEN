<template>
  <BAccordionItem v-bind="$attrs" class="t-accordion-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BAccordionItem>
</template>

<style scoped lang="scss">
.t-accordion-item :deep(.accordion-header) {
  font-weight: 700;
  letter-spacing: -0.01em;
}

.t-accordion-item :deep(.accordion-button) {
  font-size: 0.9375rem;
  color: #4a5568;
  
  &:not(.collapsed) {
    color: #2E5BFF;
  }
}
</style>
