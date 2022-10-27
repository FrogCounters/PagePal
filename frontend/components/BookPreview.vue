<template>
  <div>
    <NuxtLink :to="'/book/'+title">
      <img class="h-56 m-5 rounded-xl" :src="main_img" />
    </NuxtLink>
  </div>
</template>

<script>
export default {
  name: 'BookPreview',
  props: {
    title: {
      type: String,
      required: true,
    },
    main_img: {
      type: String,
      default: "https://upload.wikimedia.org/wikipedia/commons/thumb/6/65/No-Image-Placeholder.svg/330px-No-Image-Placeholder.svg.png",
    }
  },
}
</script>