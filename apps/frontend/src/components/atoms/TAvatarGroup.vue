<template>
  <BAvatarGroup v-bind="$attrs" class="t-avatar-group">
    <slot />
  </BAvatarGroup>
</template>

<style scoped>
.t-avatar-group :deep(.b-avatar) {
  margin-right: -0.75rem;
  z-index: 1;
  transition: all 0.2s ease-in-out;
}
.t-avatar-group :deep(.b-avatar:hover) {
  z-index: 10;
  transform: scale(1.1);
  margin-right: -0.25rem;
  margin-left: 0.25rem;
}
</style>
