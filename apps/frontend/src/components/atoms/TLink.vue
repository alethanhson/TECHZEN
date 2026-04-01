<template>
  <BLink v-bind="$attrs" class="t-link">
    <slot />
  </BLink>
</template>

<style scoped lang="scss">
.t-link {
  color: #2E5BFF;
  text-decoration: none;
  font-weight: 600;
  position: relative;
  transition: all 0.2s ease;
  padding: 2px 0;

  &:hover {
    color: #1e40af;
    opacity: 0.85;
  }

  &::after {
    content: "";
    position: absolute;
    bottom: 0;
    left: 0;
    width: 0;
    height: 2px;
    background-color: currentColor;
    transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 2px;
  }

  &:hover::after {
    width: 100%;
  }

  &.text-dark {
    color: #2d3748 !important;
    &:hover {
      color: #2E5BFF !important;
    }
  }
}
</style>
