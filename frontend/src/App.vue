<template>
  <v-app style="background-color: #224224; color: white;">
    <Navbar />
    <v-main>
      <AboutUs />
      <MainProject />
      <ContactUs />
    </v-main>
    <Footer />
  </v-app>
</template>

<script>
import Navbar from './components/NavBar.vue';
import AboutUs from './components/AboutUs.vue';
import MainProject from './components/MainProject.vue';
import ContactUs from './components/ContactUs.vue';
import Footer from './components/Footer.vue';

export default {
  name: 'App',
  components: {
    Navbar,
    AboutUs,
    MainProject,
    ContactUs,
    Footer,
  },
};
</script>

<style>
.app {
  background-color: #224224;
}
</style>
