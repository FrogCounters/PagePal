<template>
  <div class="w-full flex flex-col items-center">
    <div class="w-full max-w-5xl flex flex-row mt-16 mb-8">
      <img
        class="w-48 mr-8"
        src="~/assets/img/PuzzledGreen.png"
        alt="Puzzled green monster"
      />
      <div class="w-full">
        <h2 class="text-5xl mb-4">What is PagePal?</h2>
        <p class="text-xl">
          PagePal uses
          <a href="https://www.expert.ai/" target="_blank">expertai</a>'s natural
          language processing (NLP) API to analyse children's books and output
          emotional analysis of the different portions of the books. This helps
          to develop language-emotion associations for your child at their most
          critical stage in learning.
        </p>
      </div>
    </div>
    <div class="w-full max-w-5xl flex flex-row mt-16 mb-8">
      <div class="w-full">
        <h2 class="text-5xl mb-4">Who should use PagePal?</h2>
        <p class="text-xl">
          PagePal is suitable for children at all levels of reading. Our book
          catalogue contains a range of difficulties, and you can use our
          <NuxtLink to="/analyse">custom book upload</NuxtLink> feature to
          upload the books you wish for your child to read!
          <br />
          We encourage you to use PagePal and go through books and emotions with
          your children, but they can also use it to read for themselves if you
          wish.
        </p>
      </div>
      <img
        class="h-48 ml-8"
        src="~/assets/img/FourPeople.png"
        alt="Four monsters hand in hand"
      />
    </div>
    <div class="w-full max-w-5xl flex flex-col items-center mt-16 mb-8">
      <img
        class="w-64"
        src="~/assets/img/TornPage.png"
        alt="Monster holding book with torn page"
      />
      <h2 class="text-5xl mb-4">Let's see PagePal in action!</h2>
    </div>
    <div
      class="w-full max-w-5xl flex flex-col mb-32 rounded-lg border bg-white p-4"
    >
      <h3 class="text-3xl mb-8">
        A snippet from
        <NuxtLink to="/book/The Story of the Three Little Pigs"
          >Three Little Pigs
        </NuxtLink>
      </h3>
      <div>
        <EmoText
          :emotions="['fear']"
          text="He went to the little Pig's house, and told him how frightened had"
        />
        <EmoText
          :emotions="[]"
          text='been by a great round thing which came down the hill past him. Then the little Pig said, "Hah!'
        />
        <EmoText :emotions="['fear']" text="I frightened you, did I?" />
        <EmoText
          :emotions="[]"
          text="I had been to the Fair and bought a butter churn, and when I saw you I got into it, and rolled down the hill."
        />
        <EmoText
          :emotions="['anger']"
          text="Then the Wolf was very angry indeed, and declared he would eat up"
        />
        <EmoText :emotions="[]" text=". . ." />
      </div>
    </div>
  </div>
</template>

<style scoped>
a {
  text-decoration: underline;
  text-decoration-color: #1e7ec1;
}
</style>
