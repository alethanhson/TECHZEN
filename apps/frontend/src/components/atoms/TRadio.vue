<template>
  <BFormRadio v-bind="$attrs" class="t-radio">
    <slot />
  </BFormRadio>
</template>

<style scoped>
.t-radio :deep(.form-check-input:checked) {
  background-color: #3b82f6;
  border-color: #3b82f6;
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}
</style>
