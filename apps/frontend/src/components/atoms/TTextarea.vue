<template>
  <BFormTextarea v-bind="$attrs" class="t-textarea" />
</template>

<style scoped lang="scss">
.t-textarea {
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  background-color: #f8fafc;
  padding: 0.75rem 1rem;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  min-height: 100px;
  font-size: 0.9375rem;

  &:focus {
    background-color: #ffffff;
    border-color: #2E5BFF;
    box-shadow: 0 0 0 4px rgba(46, 91, 255, 0.1);
    outline: none;
  }
}
</style>
