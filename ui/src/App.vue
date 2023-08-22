<script setup>
import MainTable from "./components/MainTable.vue";
</script>

<template>
  <div>
    <h3 style="text-align: center; font-weight: lighter; margin: 0">JOKIC</h3>
    <MainTable />
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
