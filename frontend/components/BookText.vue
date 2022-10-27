<template>
  <div class="flex flex-col items-center p-4 pb-12">
    <div class="text-center">
      <h2 class="text-5xl font-semibold">
        {{ book.title }}
      </h2>
      <p>{{ book.author }}</p>
    </div>

    <!-- <img :src="https://upload.wikimedia.org/wikipedia/en/f/fe/CharlotteWeb.png" alt={{book.title}} /> -->
    <div class="max-w-6xl mt-8">
      <EmoText
        v-for="(text, index) in book.text"
        :key="index"
        :text="text"
        :emotions="
          book.emotions[index]
            .split(',')
            .slice(0, -1)
            .map((x) => x.toLowerCase())
        "
      />
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    book: {
      type: Object,
      required: true,
    }
  },
}
</script>