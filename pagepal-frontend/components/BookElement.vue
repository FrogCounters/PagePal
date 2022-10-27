<template>
  <div class="w-full m-6 shadow-lg bg-white">
    <NuxtLink :to="'/book/'+title">
      <div class="w-full h-32 flex flex-row flex-wrap">
        <div class="w-32">
          <img class="h-32 mr-4" :src="main_img" alt="">
        </div>
        <div class="flex flex-col">
          <h3 class="my-4 text-3xl">{{ title }}</h3>
          <p class="text-xl">{{ author }}</p>
        </div>
      </div>
    </NuxtLink>
  </div>
</template>

<script>
export default {
  name: 'BookElement',
  props: {
    title: {
      type: String,
      required: true,
    },
    author: {
      type: String,
      default: "Unknown",
    },
    main_img: {
      type: String,
      default: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/330px-No-Image-Placeholder.svg.png",
    }
  },
}
</script>