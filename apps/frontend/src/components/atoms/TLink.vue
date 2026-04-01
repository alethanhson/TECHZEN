<template>
  <BLink v-bind="$attrs" class="t-link">
    <slot />
  </BLink>
</template>

<style scoped>
.t-link {
  color: #3b82f6;
  text-decoration: none;
  font-weight: 600;
  position: relative;
  transition: color 0.2s;
}

.t-link:hover {
  color: #1d4ed8;
}

.t-link:after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  right: 0;
  height: 1px;
  background-color: currentColor;
  transform: scaleX(0);
  transition: transform 0.2s ease-in-out;
  transform-origin: right;
}

.t-link:hover:after {
  transform: scaleX(1);
  transform-origin: left;
}
</style>
