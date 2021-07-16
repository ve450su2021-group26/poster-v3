<template>
  <v-vanta effect="clouds" :options=options></v-vanta>
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
        minWidth: 200.00
      }
    }
  }
}
</script>