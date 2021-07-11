<template>
  <div>
    <b-carousel
        id="carousel-1"
        v-model="slide"
        :interval="4000"
        background="#ababab"
        controls
        fade
        img-height="480"
        img-width="1024"
        indicators
        style="text-shadow: 1px 1px 2px #333;"
        @sliding-start="onSlideStart"
        @sliding-end="onSlideEnd"
    >
      <!-- Text slides with image -->
      <b-carousel-slide
          caption="First slide"
          img-src="https://picsum.photos/1024/480/?image=52"
          text="Nulla vitae elit libero, a pharetra augue mollis interdum."
      ></b-carousel-slide>

      <!-- Slides with custom text -->
      <b-carousel-slide
          caption="Second slide"
          img-src="https://picsum.photos/1024/480/?image=54">
        <h1>Hello world!</h1>
      </b-carousel-slide>

      <!-- Slides with image only -->
      <b-carousel-slide
          caption="Third slide"
          img-src="https://picsum.photos/1024/480/?image=58"></b-carousel-slide>

      <!-- Slides with img slot -->
      <!-- Note the classes .d-block and .img-fluid to prevent browser default image alignment -->
      <b-carousel-slide
          caption="Forth slide">
        <template #img>
          <img
              alt="image slot"
              class="d-block img-fluid w-100"
              height="480"
              src="https://picsum.photos/1024/480/?image=55"
              width="1024"
          >
        </template>
      </b-carousel-slide>

      <!-- Slide with blank fluid image to maintain slide aspect ratio -->
      <b-carousel-slide caption="Fifth Slide" img-alt="Blank image" img-blank>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse eros felis, tincidunt
          a tincidunt eget, convallis vel est. Ut pellentesque ut lacus vel interdum.
        </p>
      </b-carousel-slide>
    </b-carousel>
    <br>
    <!--    <p class="mt-4">-->
    <!--      Slide #: {{ slide }}<br>-->
    <!--      Sliding: {{ sliding }}-->
    <!--    </p>-->
  </div>
</template>

<script>
export default {
  name: 'my_carousel',

  data() {
    return {
      slide: 0,
      sliding: null,
    };
  },
  methods: {
    onSlideStart(slide) {
      this.sliding = true;
    },
    onSlideEnd(slide) {
      this.sliding = false;
    },
  },
};
</script>
