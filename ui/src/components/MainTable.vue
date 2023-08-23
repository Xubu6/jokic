<template>
  <div class="q-pa-md" style="padding-top: 0">
    <q-table
      class="my-sticky-header-table"
      flat
      :dense="$q.screen.lt.md"
      :rows="rows"
      :columns="columns"
      row-key="rk"
      separator="cell"
      virtual-scroll
      hide-pagination
      :rows-per-page-options="[0]"
      :visible-columns="visibleColumns"
    >
      <template v-slot:top>
        <q-select
          class="column-select"
          v-model="visibleColumns"
          multiple
          standout
          options-dense
          options-dark
          options-selected-class="text-blue"
          display-value="Choose fields to omit"
          display-value-color="blue"
          emit-value
          map-options
          hide-bottom-space
          bg-color="primary"
          :options="columns"
          option-value="name"
        />
      </template>
      <template v-slot:body-cell-umbinaam="props">
        <q-td :props="props">
          <div>
            <q-item-section>
              <q-badge
                text-color="blue"
                :label="props.value"
                style="
                  font-weight: bolder;
                  align-self: center;
                  background-color: inherit;
                "
              />
              <!-- <q-item-label caption>
                <q-badge text-color="green" v-if="props.value">
                  {{ props.value }}
                </q-badge>
              </q-item-label> -->
            </q-item-section>
          </div>
        </q-td>
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
          align: "center",
          label: "Player",
          field: "player_name",
          style: "font-weight: bold; color: #d3d3d3; margin-right: 5px; min-width: 9vw;",
          sortable: false,
        },
        {
          name: "team_abbreviation", // Eventually replace with logos (mapping of abbreviations to .svg paths perhaps?)
          align: "center",
          label: "TEAM",
          field: "team_abbreviation",
          style: "font-weight: light; font-size: 11px",
          sortable: false,
        },
        {
          name: "min",
          align: "center",
          label: "MP",
          field: "min",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (Math.round(val * 10) / 10).toFixed(1),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "umbinaam",
          align: "center",
          label: "UMBINAAM",
          field: "umbinaam",
          style: "font-weight: light; font-size: 11px",
          required: true,
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "epm",
          align: "center",
          label: "EPM",
          field: "epm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "raptor",
          align: "center",
          label: "RAPTOR",
          field: "raptor",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "raptor_war",
          align: "center",
          label: "RWAR",
          field: "raptor_war",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "dpm",
          align: "center",
          label: "DPM",
          field: "dpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "vorp",
          align: "center",
          label: "VORP",
          field: "vorp",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "bpm",
          align: "center",
          label: "BPM",
          field: "bpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "lebron",
          align: "center",
          label: "LEBRON",
          field: "lebron",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "net_rating",
          align: "center",
          label: "NETRTG",
          field: "net_rating",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "pie",
          align: "center",
          label: "PIE",
          field: "pie",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "per",
          align: "center",
          label: "PER",
          field: "per",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "ws_per_48",
          align: "center",
          label: "WS/48",
          field: "ws_per_48",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "e_wins",
          align: "center",
          label: "EWINS",
          field: "e_wins",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "bbi_war",
          align: "center",
          label: "LeWAR",
          field: "bbi_war",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "rpm",
          align: "center",
          label: "RPM",
          field: "rpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "rpm_wins",
          align: "center",
          label: "RWINS",
          field: "rpm_wins",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "wpa",
          align: "center",
          label: "WPA",
          field: "wpa",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "k_wpa",
          align: "center",
          label: "kWPA",
          field: "k_wpa",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a - b,
        },
        {
          name: "fic",
          align: "center",
          label: "FIC",
          field: "fic",
          style: "font-weight: light; font-size: 11px",
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
        "lebron",
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
      // merge payload with standard percentile ranks
      // the color of the percentile should be

      // ADD RANKINGS TO SQL TABLE
      this.rows = payload[0];
    });
  },
  methods: {
    getColor: function (percentile) {
      //value from 0 to 1
      var hue = ((1 - percentile) * 120).toString(10);
      return ["hsl(", hue, ",100%,50%)"].join("");
    },
  },
};
</script>

<style lang="sass">
.column-select
  background-color: transparent
  text-color: white !important
  width: 12vw
  position: sticky

  .q-field__native
    color: white
  
  .q-icon
    color: white

.my-sticky-header-table

  height: 88vh
  max-width: 98vw
  margin-left: auto
  margin-right: auto

  .q-table__top
    background-image: linear-gradient(to right, #434343 0%, black 100%)
    padding-left: 0

  .q-table__bottom,
  thead tr:first-child th
    background-color: $primary

  thead tr th
    position: sticky
    z-index: 1
    color: white
    font-size: 11px
    padding: 0 !important
    text-align: center
  thead tr:first-child th
    top: 0

  thead i
    display: none

  &.q-table--loading thead tr:last-child th
    /* height of all previous header rows */
    top: 48px

  /* prevent scrolling behind sticky top row on focus */
  tbody
    /* height of all previous header rows */
    font-size: 11px
    scroll-margin-top: 48px
    background-image: linear-gradient(to right, #434343 0%, black 100%)
    color: white
    word-wrap: normal

  td
    padding: 0 !important
</style>
