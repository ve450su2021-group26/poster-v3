<template>
  <div class="hello">
    <br>
    <h2>
      Intelligent Poster Generator.
    </h2>
    <br>
    <h1>
      Make an awesome poster
      <br>
      from any image
    </h1>

    <br>

    <my_carousel></my_carousel>
    <br>

    <uploader @toParent = "getPayload"></uploader>
    <div>the payload is: {{payload}}</div>
    <div>the result is: {{result}}</div>

    <br>
    <br>
    <p>All user photo are automatically deleted
      <br>
      after being processed
    </p>
    <button type='button' class="btn btn-primary btn-lg" @click="postLoad(payload)">
      Upload</button>
    <button type='button' class="btn btn-primary btn-lg" @click="getResult()">
    Try demo photo</button>
    <table class="table table-hover">
      <thead>Results</thead>
      <tbody>
      <tr v-for="(classification, index) in result" :key="index">
        <td>{{classification}}</td>
      </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
// eslint-disable-next-line camelcase,import/extensions
import axios from 'axios';
// eslint-disable-next-line import/extensions,camelcase
import my_carousel from './carousel';
// eslint-disable-next-line import/extensions
import uploader from './uploader';

export default {
  name: 'Title',
  data() {
    return {
      payload: [],
      result: [],
    };
  },
  components: {
    my_carousel, uploader,
  },
  methods: {
    // eslint-disable-next-line camelcase
    getPayload(child_payload) {
      // eslint-disable-next-line camelcase
      this.payload = child_payload;
    },
    getResult() {
      const path = 'http://localhost:5000/algorithm';
      axios.get(path)
        .then((res) => {
          this.result = res.data.result;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    postLoad(input) {
      const path = 'http://localhost:5000/algorithm';
      axios.post(path, input)
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  // created() {
  //   this.getResult();
  // },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Knewave&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Crete+Round&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');

h1 {
  font-family: 'Merriweather', serif;
  font-size: 70px
}

h2 {
  font-family: 'Merriweather', serif;
  font-size: 30px
}

h3 {
  font-family: 'Poppins', sans-serif;
  font-size: 25px;
  color: #5cb85c;
}

p {
  color: #808080
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

</style>
