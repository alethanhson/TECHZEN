<template>
  <BAccordionItem v-bind="$attrs" class="t-accordion-item">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BAccordionItem>
</template>

<style scoped>
.t-accordion-item :deep(.accordion-header) {
  font-weight: 600;
}
</style>
