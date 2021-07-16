<template>
  <v-vanta effect="net" :options=options></v-vanta>
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
        color: 0x3f9dff,
        backgroundColor: 0x0,
        points: 20.00
      }
    }
  }
}
</script>