<template>
  <BCard v-bind="$attrs" class="t-card">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCard>
</template>

<style scoped lang="scss">
.t-card {
  --bs-card-border-radius: 12px;
  --bs-card-border-color: rgba(0, 0, 0, 0.03);
  --bs-card-cap-bg: #f8fafc;
  --bs-card-cap-color: #1e293b;
  --bs-card-box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
  
  border-radius: var(--bs-card-border-radius);
  border: 1px solid var(--bs-card-border-color);
  box-shadow: var(--bs-card-box-shadow);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
  background: white;
}

.t-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1) !important;
}

.t-card :deep(.card-header) {
  font-weight: 700;
  letter-spacing: -0.025em;
  padding: 1rem 1.5rem;
}

.t-card :deep(.card-body) {
  padding: 1.5rem;
}

.t-card :deep(.card-footer) {
  border-top: 1px solid rgba(0, 0, 0, 0.03);
  padding: 1rem 1.5rem;
}
</style>
