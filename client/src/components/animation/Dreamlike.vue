<template>
  <v-vanta effect="halo" :options=options></v-vanta>
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
        baseColor: 0x1e1e77,
        backgroundColor: 0x0,
        amplitudeFactor: 1.50,
        size: 1.60
      }
    }
  }
}
</script>