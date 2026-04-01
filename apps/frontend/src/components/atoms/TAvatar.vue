<template>
  <BAvatar v-bind="$attrs" class="t-avatar">
    <slot />
  </BAvatar>
</template>

<style scoped lang="scss">
.t-avatar {
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.08);
  border: 2px solid white;
  transition: transform 0.2s ease;

  &:hover {
    transform: scale(1.08);
    z-index: 10;
  }
}
</style>
