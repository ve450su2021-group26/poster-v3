<template>
  <div id="home">
    <div id="front">
      <Navbar/>
      <div id="title">
        <Title/>
        <ThreeTest/>
        <Gallery/>
      </div>
    </div>
  </div>
</template>

<script>
import Title from '../components/title.vue';
import Navbar from '../components/navbar.vue';
import ThreeTest from '../components/threeTest.vue';
import Gallery from '../components/gallery.vue'
export default {
  name: 'Home',
  components: {
    Title,
    Navbar,
    ThreeTest,
    Gallery,
  },
};

</script>

<style scoped>
#home {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #000000;
}

#title {
  text-align: center;
}
</style>
