<template>
  <div class="q-pa-md" style="padding: 0">
    <div class="q-gutter-y-md">
      <q-tabs
        v-model="tab"
        class="bq-gutter-y-md"
        align="justify"
        style="color: white"
        inline-label
      >
        <q-tab
          class="text-blue shadow-2"
          name="stats"
          icon="insert_chart"
          label="Stats"
        ></q-tab>
        <q-tab
          class="text-white shadow-2"
          name="about"
          icon="troubleshoot"
          label="About"
        ></q-tab>
      </q-tabs>
      <q-tab-panels v-model="tab" animated>
        <q-tab-panel name="stats">
          <main-table />
        </q-tab-panel>

        <q-tab-panel name="about">
          <about />
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </div>
</template>

<script>
import { ref } from "vue";
import MainTable from "./MainTable.vue";
import About from "./About.vue"

export default {
  components: { MainTable, About },
  setup() {
    return {
      tab: ref("stats"),
    };
  },
};
</script>

<style lang="sass">
.q-gutter-y-md
  min-width: 100vw
  background-image: linear-gradient(to right, #434343 0%, black 100%)

.q-tab-panel
  min-height: 100vh
  padding-top: 0
  background-image: linear-gradient(to right, #434343 0%, black 100%)
</style>
