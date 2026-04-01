<template>
  <BCard v-bind="$attrs" class="t-card">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCard>
</template>

<style scoped>
.t-card {
  --bs-card-border-radius: 16px;
  --bs-card-border-color: #f1f5f9;
  --bs-card-cap-bg: #f8fafc;
  --bs-card-cap-color: #1e293b;
  --bs-card-box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  
  border-radius: var(--bs-card-border-radius);
  border: 1px solid var(--bs-card-border-color);
  box-shadow: var(--bs-card-box-shadow);
  transition: transform 0.2s, box-shadow 0.2s;
  overflow: hidden;
}

.t-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
}

.t-card :deep(.card-header) {
  font-weight: 700;
  letter-spacing: -0.025em;
}

.t-card :deep(.card-footer) {
  border-top: 1px solid #f1f5f9;
}
</style>
