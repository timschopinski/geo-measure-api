<template>
  <div id="map">
    <l-map
      :zoom="zoom"
      :center="center"
      style="height: 1500px; width: 100%;"
      @click="addMarker"
    >
      <l-tile-layer
        :url="tileLayerUrl"
        :attribution="attribution"
      ></l-tile-layer>
      <l-marker
        v-for="(marker, index) in markers"
        :key="index"
        :lat-lng="marker"
      ></l-marker>
    </l-map>
    <div class="controls">
      <button @click="clearMarkers">
        Clear Markers
      </button>
      <button @click="calculateDistance" :disabled="markers.length !== 2">
        Calculate Distance
      </button>
      <button @click="calculateArea" :disabled="markers.length < 3">
        Calculate Area
      </button>
    </div>
    <div class="results" v-if="distance || area">
      <h3>Results</h3>
      <p v-if="distance">Distance: {{ distance }} meters</p>
      <p v-if="area">Area: {{ area }} square meters</p>
    </div>
  </div>
</template>

<script>
import { LMap, LTileLayer, LMarker } from "vue3-leaflet";
import "leaflet/dist/leaflet.css";
import axios from "axios";

export default {
  components: {
    LMap,
    LTileLayer,
    LMarker,
  },
  data() {
    return {
      center: [52.24730863702887, 21.01341039798862],
      zoom: 18,
      tileLayerUrl: "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      markers: [],
      distance: null,
      area: null,
    };
  },
  methods: {
    addMarker(e) {
      this.markers.push(e.latlng);
    },
    async calculateDistance() {
      const [point1, point2] = this.markers;
      try {
        const response = await axios.post("http://localhost:8000/api/calculate_distance", {
          point_1: { latitude: point1.lat, longitude: point1.lng },
          point_2: { latitude: point2.lat, longitude: point2.lng },
        });
        // Round the distance to 2 decimal places
        this.distance = (response.data.distance_m).toFixed(2);
        this.area = null;
      } catch (error) {
        console.error(error);
      }
    },
    async calculateArea() {
      try {
        const points = this.markers.map((marker) => ({
          latitude: marker.lat,
          longitude: marker.lng,
        }));
        const response = await axios.post("http://localhost:8000/api/calculate_area", {
          points,
        });
        // Round the area to 2 decimal places
        this.area = (response.data.area_sq_m).toFixed(2);
        this.distance = null;
      } catch (error) {
        console.error(error);
      }
    },
    clearMarkers() {
      this.markers = [];
      this.distance = null;
      this.area = null;
    },
  },
};
</script>

<style scoped>
#map {
  margin: 0 auto;
  width: 80%;
  height: 600px;
}

.controls {
  margin-top: 10px;
  text-align: center;
}

.controls button {
  margin: 5px;
}

.results {
  margin-top: 20px;
  text-align: center;
}

.results h3 {
  font-size: 1.5em;
  margin-bottom: 10px;
}
</style>
