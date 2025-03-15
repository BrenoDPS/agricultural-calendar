<template>
  <v-app-bar app style="background-color: rgb(15, 46, 15); color: white;" fixed>
    <span class="ml-10 mr-4 font-weight-bold">SmartAgro</span>
    <v-img
      class=""
      max-width="40"
      height="50px"
      cover
      src="https://cdn-icons-png.flaticon.com/512/4758/4758376.png"
      >
    </v-img>
    <v-spacer></v-spacer>
    <!--<div class="mr-5 text-h6 font-weight-bold">
      <span>14/11/2024</span>
    </div> -->
    <!-- <v-btn text @click="$vuetify.goTo('#about-us')">About Us</v-btn>
    <v-btn text @click="$vuetify.goTo('#main-project')">Our Project</v-btn>
    <v-btn text @click="$vuetify.goTo('#contact-us')">Contact Us</v-btn> -->
  </v-app-bar>
</template>

<script>
export default {
  name: 'Navbar',
};
</script>

<style scoped>
</style>
