<template>
  <v-vanta effect="fog" :options=options></v-vanta>
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
        highlightColor: 0x888877,
        midtoneColor: 0x886500,
        lowlightColor: 0x727272,
        baseColor: 0xffffff,
        blurFactor: 0.66,
        zoom: 1.50
      }
    }
  }
}
</script>