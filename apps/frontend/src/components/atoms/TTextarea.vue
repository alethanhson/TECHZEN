<template>
  <BFormTextarea v-bind="$attrs" class="t-textarea" />
</template>

<style scoped>
.t-textarea {
  border-radius: 12px;
  border: 1px solid #e2e8f0;
  background-color: #f8fafc;
  padding: 0.75rem 1rem;
  transition: all 0.2s;
  min-height: 100px;
}

.t-textarea:focus {
  background-color: #ffffff;
  border-color: #3b82f6;
  box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1);
}
</style>
