<template>
  <BAvatar v-bind="$attrs" class="t-avatar">
    <slot />
  </BAvatar>
</template>

<style scoped>
.t-avatar {
  box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  border: 2px solid white;
}
</style>
