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
          name: "rk",
          required: true,
          label: "#",
          align: "left",
          field: "rk",
          sortable: true,
        },
        {
          name: "player_name",
          required: true,
          align: "left",
          label: "Player",
          field: "player_name",
          sortable: true,
        },
        {
          name: "team_abbreviation",
          align: "left",
          label: "TEAM",
          field: "team_abbreviation",
          sortable: false,
        },
        { name: "min", align: "left", label: "MP", field: "min" },
        {
          name: "umbinaam",
          align: "left",
          label: "UMBINAAM",
          field: "umbinaam",
          sortable: true,
        },
        {
          name: "net_rating",
          align: "left",
          label: "NETRTG",
          field: "net_rating",
          sortable: true,
        },
        { name: "pie", align: "left", label: "PIE", field: "pie", sortable: true },
        { name: "per", align: "left", label: "PER", field: "per", sortable: true },
        {
          name: "ws_per_48",
          align: "left",
          label: "WS/48",
          field: "ws_per_48",
          sortable: true,
        },
        { name: "bpm", align: "left", label: "BPM", field: "bpm", sortable: true },
        { name: "vorp", align: "left", label: "VORP", field: "vorp", sortable: true },
        { name: "epm", align: "left", label: "EPM", field: "epm", sortable: true },
        { name: "e_wins", align: "left", label: "EWINS", field: "e_wins", sortable: true },
        { name: "lebron", align: "left", label: "LEBRON", field: "lebron", sortable: true },
        { name: "bbi_war", align: "left", label: "LeWAR", field: "bbi_war", sortable: true },
        { name: "rpm", align: "left", label: "RPM", field: "rpm", sortable: true },
        { name: "rpm_wins", align: "left", label: "RWINS", field: "rpm_wins", sortable: true },
        { name: "wpa", align: "left", label: "WPA", field: "wpa", sortable: true },
        { name: "k_wpa", align: "left", label: "kWPA", field: "k_wpa", sortable: true },
        { name: "raptor", align: "left", label: "RAPTOR", field: "raptor", sortable: true },
        {
          name: "raptor_war",
          align: "left",
          label: "RWAR",
          field: "raptor_war",
          sortable: true,
        },
        { name: "fic", align: "left", label: "FIC", field: "fic", sortable: true },
        { name: "dpm", align: "left", label: "DPM", field: "dpm", sortable: true },
      ],
      rows: [],
      visibleColumns: [
        "player_name",
        "team_abbreviation",
        "umbinaam",
        "net_rating",
        "pie",
        "per",
        "ws_per_48",
        "bpm",
        "vorp",
        "epm",
        "e_wins",
        "lebron",
        "bbi_war",
        "rpm",
        "rpm_wins",
        "wpa",
        "k_wpa",
        "raptor",
        "raptor_war",
        "fic",
        "dpm",
      ],
    };
  },
  mounted() {
    axios.get("/data/all").then((res) => {
      const payload = res.data;
      this.rows = payload[0];
    });
  },
  methods: {
    setFieldsAndRows() {
      for (const [key, value] of Object.entries(this.rows)) {
        if (this.fields.length == 0) {
          this.fields.push(key);
          break;
        }
      }
    },
  },
};
</script>

<style lang="sass">
// div
//   color: $secondary
//   background-color: $primary

.my-sticky-header-table

  height: 80vh

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
