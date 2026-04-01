<template>
  <BFormRadioGroup v-bind="$attrs" class="t-radio-group">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BFormRadioGroup>
</template>

<style scoped lang="scss">
.t-radio-group {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;

  :deep(.form-check-input) {
    border: 2px solid #e2e8f0;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    
    &:checked {
      background-color: #2E5BFF;
      border-color: #2E5BFF;
      box-shadow: 0 4px 10px rgba(46, 91, 255, 0.2);
    }
    
    &:focus {
      box-shadow: 0 0 0 4px rgba(46, 91, 255, 0.1);
    }
  }

  :deep(.form-check-label) {
    font-weight: 500;
    color: #4a5568;
    padding-left: 0.25rem;
    cursor: pointer;
  }
}
</style>
