<template>
  <div class="q-pa-md" style="padding-top: 0">
    <q-table
      class="my-sticky-header-table"
      dark
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
      :loading="loading"
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
      <template v-slot:body-cell="props">
        <q-td :props="props">
          {{ props.value[0] ? props.value[0] : "--" }}
          <q-item-label caption>
            <q-badge
              text-color="lightgrey"
              v-if="props.value"
              style="font-size: 9px"
            >
              {{ props.value[1] && props.value[0] ? props.value[1] : "" }}
            </q-badge>
          </q-item-label>
        </q-td>
      </template>
      <template v-slot:body-cell-umbinaam="props">
        <q-td :props="props">
          <div>
            <q-item-section>
              <q-badge
                text-color="blue"
                :label="props.value[0] ? props.value[0] : '--'"
                style="
                  font-weight: bolder;
                  align-self: center;
                  background-color: inherit;
                "
              />
              <q-item-label caption>
                <q-badge
                  text-color="lightgrey"
                  v-if="props.value"
                  style="font-size: 9px"
                >
                  {{ props.value[1] && props.value[0] ? props.value[1] : "" }}
                </q-badge>
              </q-item-label>
            </q-item-section>
          </div>
        </q-td>
      </template>
      <template v-slot:body-cell-player_name="props">
        <q-td :props="props">
          {{ props.value[0] ? props.value[0] : "--" }}
          <q-item-label caption>
            <q-badge
              text-color="lightgrey"
              v-if="props.value"
              style="background-color: inherit"
            >
            </q-badge>
          </q-item-label>
        </q-td>
      </template>
      <template v-slot:body-cell-team_abbreviation="props">
        <q-td :props="props">
          {{ props.value[0] ? props.value[0] : "--" }}
          <q-item-label caption>
            <q-badge
              text-color="lightgrey"
              v-if="props.value"
              style="background-color: inherit"
            >
            </q-badge>
          </q-item-label>
        </q-td>
      </template>
    </q-table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    player_data: {},
  },
  data() {
    return {
      playerData: {},
      loading: false,
      columns: [
        {
          name: "player_name",
          required: true,
          align: "center",
          label: "Player",
          field: "player_name",
          style:
            "font-weight: bold; color: #d3d3d3; width: 10vw; max-width: 10vw; overflow: hidden",
          sortable: true,
        },
        {
          name: "team_abbreviation", // Eventually replace with logos (mapping of abbreviations to .svg paths perhaps?)
          align: "center",
          label: "TEAM",
          field: "team_abbreviation",
          style: "font-weight: light; font-size: 13px",
          sortable: false,
        },
        {
          name: "min",
          align: "center",
          label: "MP",
          field: "min",
          style: "font-weight: light; font-size: 11px",
          format: (val) => [(Math.round(val[0] * 10) / 10).toFixed(1), val[1]],
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "umbinaam",
          align: "center",
          label: "UMBINAAM",
          field: "umbinaam",
          style: "font-weight: light; font-size: 11px",
          required: true,
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "epm",
          align: "center",
          label: "EPM",
          field: "epm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "raptor",
          align: "center",
          label: "RAPTOR",
          field: "raptor",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "raptor_war",
          align: "center",
          label: "RWAR",
          field: "raptor_war",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "dpm",
          align: "center",
          label: "DPM",
          field: "dpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "vorp",
          align: "center",
          label: "VORP",
          field: "vorp",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "bpm",
          align: "center",
          label: "BPM",
          field: "bpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "lebron",
          align: "center",
          label: "LEBRON",
          field: "lebron",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "net_rating",
          align: "center",
          label: "NETRTG",
          field: "net_rating",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "pie",
          align: "center",
          label: "PIE",
          field: "pie",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "per",
          align: "center",
          label: "PER",
          field: "per",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "ws_per_48",
          align: "center",
          label: "WS/48",
          field: "ws_per_48",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "e_wins",
          align: "center",
          label: "EWINS",
          field: "e_wins",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "bbi_war",
          align: "center",
          label: "LeWAR",
          field: "bbi_war",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "rpm",
          align: "center",
          label: "RPM",
          field: "rpm",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "rpm_wins",
          align: "center",
          label: "RWINS",
          field: "rpm_wins",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "wpa",
          align: "center",
          label: "WPA",
          field: "wpa",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "k_wpa",
          align: "center",
          label: "kWPA",
          field: "k_wpa",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
        },
        {
          name: "fic",
          align: "center",
          label: "FIC",
          field: "fic",
          style: "font-weight: light; font-size: 11px",
          format: (val) => (val ? val : "--"),
          sortable: true,
          sort: (a, b) => a[0] - b[0],
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
      ranks: [],
    };
  },
  mounted() {
    // local variables for convenience
    let site_data = [];
    let rank_data = [];
    axios
      .get("/data/all")
      .then((res) => {
        const payload = res.data;
        site_data = payload[0];
        console.log(site_data);
        console.log(typeof site_data);
        this.rows = site_data;
      })
      .catch(function (error) {
        console.log(
          "Something went wrong fetching site data:",
          JSON.stringify(error)
        );
      });
    axios
      .get("/data/ranks")
      .then((response) => {
        rank_data = response.data[0];
        console.log("ranks response:", rank_data);
        this.ranks = rank_data;
        this.mergeRank(site_data, rank_data);
        const qt = document.getElementsByClassName("q-table__middle").item(0);
        Object.keys(window).forEach((key) => {
          if (/^on/.test(key)) {
            qt.addEventListener(key.slice(2), (event) => {
              this.changeColors();
            });
          }
        });
        this.changeColors();
      })
      .catch(function (error) {
        console.log(
          "Something went wrong fetching rank data:",
          JSON.stringify(error)
        );
      });
  },
  methods: {
    getColor: function (percentile) {
      if (percentile === 0) {
        return "#000000";
      }
      let hue = ((1 - percentile) * 120).toString(10);
      return ["hsl(", hue, ",80%,50%)"].join("");
    },
    changeColors: function () {
      this.loading = true;
      const num_players = this.rows.length;
      let rank_labels = document.getElementsByClassName("q-badge flex inline");
      console.log("Rank Labels:", rank_labels, rank_labels.length);
      for (var i = rank_labels.length - 1; i > -1; i--) {
        const rank_val = rank_labels[i].innerHTML
          ? parseInt(rank_labels[i].innerHTML)
          : 0;
        const percentile = rank_val / num_players;
        rank_labels[i].style.color = this.getColor(percentile);
      }
      this.loading = false;
    },
    mergeRank: function (site_data, rank_data) {
      console.log("Players:", site_data);
      console.log("Ranks:", rank_data);
      rank_data = Array.from(rank_data);
      const merged_data = [];
      site_data.forEach((row) => {
        let cur_row = {};
        const cur_name = row["player_name"];
        const rank_row = rank_data.find((x) => x.player_name === cur_name);
        for (const [field, val] of Object.entries(row)) {
          const rank_field = field + "_rank";
          const field_rank = rank_row[rank_field];
          if (Number.isInteger(field_rank)) {
            cur_row[field] = [val, field_rank];
          } else {
            cur_row[field] = [val, ""];
          }
        }
        merged_data.push(cur_row);
      });
      console.log("Merged Data:", merged_data);
      this.rows = merged_data;
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

  height: 91vh
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
    color: green
    background-color: green
    top: 148px

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
