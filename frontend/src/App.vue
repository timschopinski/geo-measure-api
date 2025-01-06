<template>
  <div id="app">
    <h1>Geo Measure App</h1>
    <MapComponent />
  </div>
</template>

<script>
import MapComponent from "./components/MapComponent.vue";

export default {
  components: {
    MapComponent,
  },
};
</script>
