<template>
  <BFormRadio v-bind="$attrs" class="t-radio">
    <slot />
  </BFormRadio>
</template>

<style scoped lang="scss">
.t-radio :deep(.form-check-input) {
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
</style>
