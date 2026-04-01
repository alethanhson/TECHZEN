<template>
  <BToast v-bind="$attrs" class="t-toast">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BToast>
</template>

<style scoped>
.t-toast :deep(.toast) {
  border-radius: 12px;
  border: none;
  background-color: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(12px);
  box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
}

.t-toast :deep(.toast-header) {
  background-color: transparent;
  border-bottom: 1px solid #f1f5f9;
  padding: 0.75rem 1rem;
  font-weight: 700;
  color: #1e293b;
}

.t-toast :deep(.toast-body) {
  padding: 1rem;
  color: #475569;
}
</style>
