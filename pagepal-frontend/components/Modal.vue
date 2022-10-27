<template>
  <div class="modal-overlay" @click="$emit('close-modal')">
    <div class="modal" @click.stop>
      <h6>Saved!</h6>
      <p>Your Story has been saved!</p>
      <p>Book ID: <NuxtLink :to="'/book/user/' + custom_url">{{custom_url}}</NuxtLink></p>
      <p>
        <button class="text-white font-bold py-2 px-4 border rounded" @click="copy">{{has_copied ? "Copied" : "Copy"}}</button>
        <button class="text-white font-bold py-2 px-4 border rounded" @click="$emit('close-modal')">Close</button>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Modal',
  props: {
    custom_url: {
      type: String,
      required: true,
    }
  },
  data() {
    return {
      has_copied: false,
    }
  },
  methods: {
    copy() {
      navigator.clipboard.writeText("https://main.d2s3ylptdaf8im.amplifyapp.com/book/user/" + this.custom_url);
      this.has_copied = true
    }
  }
}
</script>

<style scoped>
a {
  text-decoration: underline;
  text-decoration-color: rgb(47, 177, 149);
}

.modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  background-color: #454242da;
}

.modal {
  text-align: center;
  background-color: white;
  height: 60vh;
  width: 40vw;
  min-width: 300px;
  margin-top: 10vh;
  padding: 60px 0;
  border-radius: 20px;
}

h6 {
  font-weight: 500;
  font-size: 28px;
  margin: 20px 0;
}

p {
  font-size: 16px;
  margin: 20px 0;
}

button {
  background: #2FB195;
}
</style>