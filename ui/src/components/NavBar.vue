<template>
  <div class="q-pa-md" style="padding: 0">
    <div class="q-gutter-y-md" style="min-width: 100vw; height: 5vw;">
      <q-tabs v-model="tab" class="bg-grey-9" align="justify">
        <q-tab
          class="text-white"
          name="mails"
          icon="mail"
          label="Mails"
        ></q-tab>
        <q-tab
          class="text-blue"
          name="alarms"
          icon="alarm"
          label="Alarms"
        ></q-tab>
        <q-tab
          class="text-indigo"
          name="movies"
          icon="movie"
          label="Movies"
        ></q-tab>
      </q-tabs>
    </div>
  </div>
</template>


<script>
import { ref } from 'vue'

export default {
  setup () {
    return {
      tab: ref('mails')
    }
  }
}
</script>
