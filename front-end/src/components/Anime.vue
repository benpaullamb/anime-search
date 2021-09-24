<template>
  <div class="anime">
    <div class="image-container">
      <img :src="anime.posterImage.original" alt="Anime poster image">
    </div>
    <div class="details">
      <h3>{{anime.titles.en || anime.titles.en_us || anime.canonicalTitle}}</h3>
      
      <div class="meta">
        <pill>Rating: {{anime.averageRating}}/100</pill>
        <pill>Started: {{anime.startDate}}</pill>
        <pill>Episodes: {{anime.episodeCount}}</pill>
        <pill>Length: {{anime.episodeLength}}mins</pill>
      </div>

      <p>{{anime.description}}</p>
    </div>
  </div>
</template>

<script>
import Pill from './Pill.vue';

export default {
  components: {
    Pill
  },
  props: {
    anime: {
      type: Object,
      required: true
    }
  }
}
</script>

<style lang="scss">
.anime {
  display: grid;
  grid-template-columns: auto 1fr;

  .image-container {
    img {
      max-width: 200px;
    }
  }

  .details {
    padding: 1rem;

    h3 {
      margin-bottom: 0.5rem;
      font-size: 24px;
    }

    .meta {
      margin-bottom: 1rem;
      display: flex;

      .pill {
        margin-right: 0.5rem;
      }
    }
  }
}
</style>