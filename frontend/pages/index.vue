<template>
  <div>
    <!-- Header -->
    <div class="w-full flex flex-col items-center p-20">
      <div
        class="max-w-4xl w-full flex flex-row flex-wrap justify-center items-center mx-auto"
      >
        <img
          class="w-80"
          src="~/assets/img/GreenReadBook.png"
          alt="Green creature reading book"
        />
        <div class="w-96 -ml-12">
          <h2 class="text-5xl font-semibold text-center">
            Making emotional<br />development easy!
          </h2>
        </div>
      </div>
      <div class="max-w-3xl py-24 text-2xl text-center">
        PagePal is the emotional development tool for your child.
        <br />
        Start right away with one of our books!
      </div>
      <div>
        <img class="w-64 mx-auto" src="~/assets/img/BookThumbsUp.png" alt="Green thumbs up">
        <NuxtLink to="#">
          <div class="rounded-lg shadow hover:shadow-xl button p-4">
            <p class="text-2xl font-bold text-center text-white">Start reading now!</p>
          </div>
        </NuxtLink>
      </div>
    </div>
    <!-- Bottom -->
    <div class="w-full flex flex-col items-center p-20">
      <div class="max-w-6xl w-full flex flex-col">
        <h2 class="text-5xl font-semibold">More books</h2>
        <div class="w-full mt-5 flex flex-row flex-wrap">
          <BookPreview v-for="book in books" :key="book.title" :title="book.title" :main_img="book.main_img" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  data() {
    return {
      books: []
    }
  },
  methods: {
    getPosts() {
      fetch('https://bookpal1.herokuapp.com/books/')
        .then(response => response.json())
        .then(data => this.books = data["books"])
    }
  },
  mounted() {
    this.getPosts()
  }
}
</script>

<style scoped>
.accent-underline {
  text-decoration-color: #2FB195;
}

.button {
  background-color: #F6A50C;
}

.button:hover {
  background-color: #f6a000;
}
</style>
