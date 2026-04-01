<template>
  <BModal v-bind="$attrs" class="t-modal">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BModal>
</template>

<style scoped>
.t-modal :deep(.modal-content) {
  border-radius: 20px;
  border: none;
  box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.25);
  overflow: hidden;
}

.t-modal :deep(.modal-header) {
  border-bottom: 1px solid #f1f5f9;
  background-color: #f8fafc;
  padding: 1.5rem;
}

.t-modal :deep(.modal-title) {
  font-weight: 800;
  letter-spacing: -0.025em;
  color: #1e293b;
}

.t-modal :deep(.modal-body) {
  padding: 2rem 1.5rem;
  color: #475569;
  line-height: 1.6;
}

.t-modal :deep(.modal-footer) {
  border-top: 1px solid #f1f5f9;
  padding: 1rem 1.5rem;
  background-color: #f8fafc;
}
</style>
