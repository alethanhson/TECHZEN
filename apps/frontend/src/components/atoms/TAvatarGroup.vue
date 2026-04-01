<template>
  <BAvatarGroup v-bind="$attrs" class="t-avatar-group">
    <slot />
  </BAvatarGroup>
</template>

<style scoped lang="scss">
.t-avatar-group :deep(.b-avatar) {
  margin-right: -0.85rem;
  z-index: 1;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: 2px solid white;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.t-avatar-group :deep(.b-avatar:hover) {
  z-index: 10;
  transform: scale(1.15) translateY(-2px);
  margin-right: -0.35rem;
  margin-left: 0.35rem;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
}
</style>
