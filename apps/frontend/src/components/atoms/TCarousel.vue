<template>
  <BCarousel v-bind="$attrs" class="t-carousel">
    <template v-for="(_, name) in $slots" #[name]="slotData">
      <slot :name="name" v-bind="slotData || {}" />
    </template>
  </BCarousel>
</template>

<style scoped>
.t-carousel {
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
}

.t-carousel :deep(.carousel-control-prev-icon),
.t-carousel :deep(.carousel-control-next-icon) {
  background-color: rgba(30, 41, 59, 0.5);
  border-radius: 50%;
  padding: 1.5rem;
  background-size: 50%;
}

.t-carousel :deep(.carousel-indicators [data-bs-target]) {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  margin: 0 4px;
}
</style>
