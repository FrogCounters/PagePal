<template>
  <div class="inline relative">
    <div
      v-if="emotions.length"
      class="absolute px-1 inline -top-8 rounded-lg border-2 bg-white whitespace-nowrap"
    >
      <span v-for="emotion in emotions" :key="emotion" class="capitalize">
        {{ emotion }}
        <i :class="['twa', toEmoji(emotion)]"></i>
      </span>
    </div>
    <span
      :class="
        ['text', 'inline', 'mt-4', 'text-xl'].concat(
          emotions.map((x) => 'emotion-' + x)
        )
      "
      >{{ text }}</span
    >&nbsp;
  </div>
</template>

<script>
export default {
  name: 'EmoText',
  props: {
    text: {
      type: String,
      required: true,
    },
    emotions: {
      type: Array,
      required: true,
    },
  },
  methods: {
    toEmoji(emotion) {
      // for now we only do emoji for first emotion
      let mapping = {
        anger: 'twa-rage',
        fear: 'twa-fearful',
        happiness: 'twa-relaxed',
        sadness: 'twa-cry',
        hatred: 'twa-imp',
        like: 'twa-smiley',
        joy: 'twa-joy',
        love: 'twa-heart-eyes',
        affection: 'twa-heart-eyes',
        amusement: 'twa-laughing',
        satisfaction: 'twa-satisfied',
        anxiety: 'twa-confounded',
        surprise: 'twa-open-mouth',
        shame: 'twa-sweat',
        irritation: 'twa-angry',
        regret: 'twa-sob',
        excited: 'twa-grin',
        suffering: 'twa-tired_face',
        disgust: 'twa-scream',
        offence: 'twa-unamused',
        disappointment: 'twa-anguished',
      }
      return mapping[emotion] ?? 'twa-question'
    },
  },
}
</script>

<style scoped>
.text {
  line-height: 3.5rem;
}

/* rage */
.emotion-anger {
  background-color: hsla(0, 58%, 70%, 1);
}
.emotion-irritation {
  background-color: hsla(0, 58%, 70%, 1);
}
.emotion-exasperation {
  background-color: hsla(0, 58%, 70%, 1);
}

/* apprehension */
.emotion-anxiety {
  background-color: hsla(318, 58%, 70%, 1);
}
.emotion-fear {
  background-color: hsla(318, 58%, 70%, 1);
}
.emotion-stress {
  background-color: hsla(318, 58%, 70%, 1);
}
.emotion-worry {
  background-color: hsla(318, 58%, 70%, 1);
}

/* distress */
.emotion-disgust {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-repulsion {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-guilt {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-shame {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-embarrassment {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-regret {
  background-color: hsla(22, 58%, 70%, 1);
}
.emotion-boredom {
  background-color: hsla(22, 58%, 70%, 1);
}

/* resentment */
.emotion-hatred {
  background-color: hsla(342, 58%, 70%, 1);
}
.emotion-offence {
  background-color: hsla(342, 58%, 70%, 1);
}
.emotion-jealousy {
  background-color: hsla(84, 58%, 70%, 1);
}
.emotion-envy {
  background-color: hsla(84, 58%, 70%, 1);
}

/* dejection */
.emotion-sadness {
  background-color: hsla(228, 58%, 70%, 1);
}
.emotion-torment {
  background-color: hsla(228, 58%, 70%, 1);
}
.emotion-suffering {
  background-color: hsla(228, 58%, 70%, 1);
}
.emotion-disappointment {
  background-color: hsla(228, 58%, 70%, 1);
}
.emotion-disillusion {
  background-color: hsla(228, 58%, 70%, 1);
}
.emotion-resignation {
  background-color: hsla(228, 58%, 70%, 1);
}

/* surprise */
.emotion-surprise {
  background-color: coral;
}

/* delight */
.emotion-happiness {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-excitement {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-joy {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-amusement {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-well-being {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-satisfaction {
  background-color: hsla(141, 58%, 70%, 1);
}
.emotion-relief {
  background-color: hsla(141, 58%, 70%, 1);
}

/* fondness */
.emotion-like {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-trust {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-affection {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-love {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-passion {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-empathy {
  background-color: hsla(127, 58%, 70%, 1);
}
.emotion-compassion {
  background-color: hsla(127, 58%, 70%, 1);
}
</style>
