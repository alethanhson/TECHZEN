<template>
  <BCarousel v-bind="$attrs" class="t-carousel">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCarousel>
</template>

<style scoped lang="scss">
.t-carousel {
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
  border: 1px solid rgba(0, 0, 0, 0.03);
}

.t-carousel :deep(.carousel-control-prev-icon),
.t-carousel :deep(.carousel-control-next-icon) {
  background-color: rgba(255, 255, 255, 0.6);
  border-radius: 50%;
  padding: 1.25rem;
  background-size: 50%;
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  color: #1a202c;
  
  &:hover {
    background-color: white;
    transform: scale(1.1);
  }
}

.t-carousel :deep(.carousel-indicators [data-bs-target]) {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  margin: 0 6px;
  background-color: rgba(255, 255, 255, 0.5);
  border: 2px solid rgba(0, 0, 0, 0.1);
  
  &.active {
    background-color: #2E5BFF;
    transform: scale(1.2);
  }
}
</style>
