<script setup>
import MainTable from "./components/MainTable.vue";
import NavBar from "./components/NavBar.vue"
</script>

<template>
  <div class="container">
    <NavBar />
    <!-- <h3 style="text-align: center; font-weight: lighter; margin: 0; color: white; padding-top: 10px; padding-bottom: 10px">JOKIC</h3> -->
    <!-- tiles that can be expanded to learn about each stat, specifically umbinaam (perhaps ?) "Weightings based on sophisticated sentiment analysis" lmao-->
    <MainTable />
  </div>
</template>

<style scoped>
  .container {
    min-height: 100vh;
    /* background-color: #121212; */
    background-image: linear-gradient(to right, #434343 0%, black 100%);
  }
</style>
