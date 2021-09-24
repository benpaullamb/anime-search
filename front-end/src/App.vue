<template>
  <div class="container">
    <div class="container__page">
      <header>
        <h1>Anime Search</h1>
        <span>with Python</span>
        <input v-model="searchText" @keydown.enter="search" type="text" placeholder="Search...">
      </header>

      <div v-if="animes.length > 0" class="results">
        <h2>Results</h2>

        <anime v-for="(anime, i) in animes" :key="`anime-${i}`" :anime="anime" class="results__anime"/>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Anime from './components/Anime.vue';

export default {
  name: 'App',
  components: {
    Anime
  },
  data() {
    return {
      searchText: '',
      animes: []
    };
  },
  methods: {
    async search() {
      try {
        const response = await axios({
          method: 'GET',
          url: `/anime/search/${this.searchText}`
        });
        this.animes = response.data.data.map(anime => anime.attributes);
        console.log(this.animes);
      } catch(err) {
        this.animes = [];
        console.error(err);
      }
    }
  }
}
</script>

<style lang="scss">
* {
  box-sizing: border-box;
  padding: 0;
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.container {
  display: flex;
  justify-content: center;

  .container__page {
    max-width: 75%;
    padding: 2rem;
  }
}

header {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;

  h1 {
    margin-bottom: 0.5rem;
    font-size: 48px;
  }

  span {
    margin-bottom: 1rem;
    font-size: 16px;
  }

  input {
    padding: 0.5rem;
    border: 1px solid grey;
    border-radius: 8px;
    font-size: 20px;
  }
}

.results {
  h2 {
    margin-bottom: 1rem;
    font-size: 34px;
  }

  .results__anime {
    margin-bottom: 1rem;
  }
}
</style>
