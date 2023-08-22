<template>
  <div class="q-pa-md">
    <q-table
      class="my-sticky-header-table"
      flat
      bordered
      :dense="$q.screen.lt.md"
      :rows="rows"
      :columns="columns"
      row-key="rk"
      separator="cell"
      virtual-scroll
      :rows-per-page-options="[0]"
      :visible-columns="visibleColumns"
    >
      <template v-slot:top>
        <span>Jokic</span>

        <q-space />

        <q-select
          v-model="visibleColumns"
          multiple
          outlined
          dense
          options-dense
          :display-value="$q.lang.table.columns"
          emit-value
          map-options
          :options="columns"
          option-value="name"
          options-cover
        />
      </template>
    </q-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      playerData: {},
      columns: [
        {
          name: "player_name",
          required: true,
          align: "left",
          label: "Player",
          field: "player_name",
          sortable: false,
        },
        {
          name: "team_abbreviation",
          align: "left",
          label: "TEAM",
          field: "team_abbreviation",
          sortable: false,
        },
        {
          name: "min",
          align: "left",
          label: "MP",
          field: "min",
          format: (val) => (Math.round(val * 10) / 10).toFixed(1),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "umbinaam",
          align: "left",
          label: "UMBINAAM",
          field: "umbinaam",
          required: true,
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "epm",
          align: "left",
          label: "EPM",
          field: "epm",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "raptor",
          align: "left",
          label: "RAPTOR",
          field: "raptor",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "raptor_war",
          align: "left",
          label: "RWAR",
          field: "raptor_war",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "dpm",
          align: "left",
          label: "DPM",
          field: "dpm",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "vorp",
          align: "left",
          label: "VORP",
          field: "vorp",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "bpm",
          align: "left",
          label: "BPM",
          field: "bpm",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "lebron",
          align: "left",
          label: "LEBRON",
          field: "lebron",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "net_rating",
          align: "left",
          label: "NETRTG",
          field: "net_rating",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "pie",
          align: "left",
          label: "PIE",
          field: "pie",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "per",
          align: "left",
          label: "PER",
          field: "per",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "ws_per_48",
          align: "left",
          label: "WS/48",
          field: "ws_per_48",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "e_wins",
          align: "left",
          label: "EWINS",
          field: "e_wins",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "bbi_war",
          align: "left",
          label: "LeWAR",
          field: "bbi_war",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "rpm",
          align: "left",
          label: "RPM",
          field: "rpm",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "rpm_wins",
          align: "left",
          label: "RWINS",
          field: "rpm_wins",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "wpa",
          align: "left",
          label: "WPA",
          field: "wpa",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "k_wpa",
          align: "left",
          label: "kWPA",
          field: "k_wpa",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "fic",
          align: "left",
          label: "FIC",
          field: "fic",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
      ],
      rows: [],
      visibleColumns: [
        "player_name",
        "team_abbreviation",
        "min",
        "umbinaam",
        "epm",
        "raptor",
        "raptor_war",
        "dpm",
        "vorp",
        "bpm",
        "LEBRON",
        "net_rating",
        "pie",
        "per",
        "ws_per_48",
        "e_wins",
        "bbi_war",
        "rpm",
        "rpm_wins",
        "wpa",
        "k_wpa",
        "fic",
      ],
    };
  },
  mounted() {
    axios.get("/data/all").then((res) => {
      const payload = res.data;
      console.log(payload[0]);
      this.rows = payload[0];
    });
  },
};
</script>

<style lang="sass">
// div
//   color: $secondary
//   background-color: $primary

.my-sticky-header-table

  height: 90vh

  .q-table__top,
  .q-table__bottom,
  thead tr:first-child th
    background-color: $secondary

  thead tr th
    position: sticky
    z-index: 1
    color: white
  thead tr:first-child th
    top: 0

  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px

  /* prevent scrolling behind sticky top row on focus */
  tbody
    /* height of all previous header rows */
    scroll-margin-top: 48px
    background-color: $primary
    color: white
    word-wrap: break-word
</style>
