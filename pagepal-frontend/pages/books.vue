<template>
  <div class="w-full flex flex-col items-center">
    <div class="w-full max-w-4xl flex flex-col mt-16 mb-8">
      <h2 class="text-5xl font-semibold">Our Catalogue</h2>
    </div>
    <div class="w-full max-w-4xl mx-auto flex flex-col items-center p-4">
      <BookElement v-for="book in books" :key="book.title" :title="book.title" :author="book.author" :main_img="book.main_img" />
    </div>
  </div>
</template>


<script>
export default {
  name: 'BooksPage',
  data() {
    return {
      books: []
    }
  },
  methods: {
    getBooks() {
      fetch('https://bookpal1.herokuapp.com/books/')
        .then(response => response.json())
        .then(data => this.books = data["books"])
    }
  },
  mounted() {
    this.getBooks()
  }
}
</script>