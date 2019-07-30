<template>
  <v-container>
    <v-layout
      text-center
      wrap
    >
      <v-flex mb-4>
        <h1 class="display-2 font-weight-bold mb-3">
          Airconditioner controller
        </h1>
        <div class="subheading font-weight-regular">
          <v-btn
            color="primary"
            large
            dark
            @click="start"
          >
            Start
          </v-btn>
          <v-btn
            color="primary"
            large
            dark
            @click="stop"
          >
            Stop
          </v-btn>
          <v-btn
            color="primary"
            large
            dark
            @click="getSensorInfo"
          >
            Get sensor info
          </v-btn>

        </div>
        <div>
          {{sensorInfo}}
        </div>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data: () => ({
    powerStatus: null,
    sensorInfo: {},
  }),
  methods: {

    start: function(){
      axios.get(`${process.env.VUE_APP_AIRCON_URL}/power/start`)
    },

    stop: function(){
      axios.get(`${process.env.VUE_APP_AIRCON_URL}/power/stop`)
    },

    status: function(){
      axios.get(`${process.env.VUE_APP_AIRCON_URL}/power/status`)
    },

    getSensorInfo: function(){
      axios.get(`${process.env.VUE_APP_AIRCON_URL}/sensor/info`)
      .then( (response) => {
        this.$set(this, 'sensorInfo', response.data)
      })
      .catch( () => {
        this.$set(this, 'sensorInfo', {})
      })
    }

  }
};
</script>
