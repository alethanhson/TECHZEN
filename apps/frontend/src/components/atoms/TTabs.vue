<template>
  <BTabs v-bind="$attrs" class="t-tabs">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BTabs>
</template>

<style scoped lang="scss">
.t-tabs :deep(.nav-tabs) {
  border-bottom: 2px solid #edf2f7;
  gap: 0.5rem;
  padding: 0 1rem;
}

.t-tabs :deep(.nav-link) {
  border: none;
  font-weight: 600;
  color: #718096;
  padding: 1rem 1.5rem;
  border-radius: 10px 10px 0 0;
  position: relative;
  transition: all 0.3s ease;
  font-size: 0.9375rem;

  &:hover {
    color: #2E5BFF;
    background-color: rgba(46, 91, 255, 0.04);
  }

  &.active {
    background-color: transparent;
    color: #2E5BFF;

    &::after {
      content: "";
      position: absolute;
      bottom: -2px;
      left: 0;
      right: 0;
      height: 3px;
      background-color: #2E5BFF;
      border-radius: 3px 3px 0 0;
    }
  }
}

.t-tabs :deep(.tab-content) {
  padding: 2rem 1rem;
  color: #4a5568;
}
</style>
