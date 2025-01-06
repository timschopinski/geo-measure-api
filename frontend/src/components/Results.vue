<template>
  <div>
    <h2>Results</h2>
    <p v-if="distance">Distance: {{ distance }} meters</p>
    <p v-if="area">Area: {{ area }} square meters</p>
  </div>
</template>

<script>
export default {
  props: {
    distance: {
      type: Number,
      required: false,
    },
    area: {
      type: Number,
      required: false,
    },
  },
};
</script>
