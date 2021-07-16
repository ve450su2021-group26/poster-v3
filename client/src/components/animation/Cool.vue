<template>
  <v-vanta effect="rings" :options=options></v-vanta>
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
        scaleMobile: 1.00
      }
    }
  }
}
</script>