<template>
  <v-vanta effect="waves" :options=options></v-vanta>
</template>

<script>
import VVanta from 'vue-vanta/src/Vanta.vue';
export default {
  components: { VVanta },
  data () {
    return {
      options: {
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 880.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        color: 0x1b5e,
        shininess: 64.00,
        waveHeight: 17.00,
        waveSpeed: 0.85,
        zoom: 1.00
      }
    }
  }
}
</script>