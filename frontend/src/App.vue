<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>AirCon</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>

    <v-content>
      <AirCon/>
    </v-content>
  </v-app>
</template>

<script>
import AirCon from '@/components/AirCon'

export default {
  name: 'App',
  components: {
    AirCon,
  },
  data: () => ({
    //
  }),
};
</script>
