<template>
  <v-vanta effect='birds' :options=options></v-vanta>
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
        birdSize: 1.50,
        scaleMobile: 1.00,
        backgroundColor: 0xffffff,
        color2: 0xff6000,
        wingSpan: 20.00,
        speedLimit: 7.00,
        separation: 49.00,
        alignment: 1.00,
        cohesion: 1.00
      }
    }
  }
}
</script>