<template>
  <div>
    <div v-for="note in notes" :key="note">
      {{note}}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'App',
  data: () => ({
    notes: []
  }),
  components: {
    
  },
  mounted () {
  axios.get('http://localhost:8000/api/notes/').then((response) => {
    this.notes = response.data;
  })
}
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
