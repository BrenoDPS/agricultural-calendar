<template>
  <v-container id="about-us" class="mt-12">
    <v-row>
      <v-col>
        <v-img
          class=""
          width="580"
          height="400px"
          aspect-ratio="16/9"
          cover
          src="https://cdn.pixabay.com/photo/2021/09/18/02/27/vietnam-6634082_1280.jpg"
          >
        </v-img>
        <!-- src="https://t3.ftcdn.net/jpg/07/71/59/00/360_F_771590016_jsW2fQ0gWYxyG03hmILDgPnJUU0Xl5mc.jpg" -->
      </v-col>
      <v-col>
        <!-- <div class="d-flex">
          <p class="text-h3 font-weight-bold">Sobre Nós</p>
        </div> -->
        <div>
          <div class="mt-12">
            <span class="text-h6">
              Nosso site oferece uma ferramenta prática e acessível para agricultores, simplificando o planejamento agrícola com calendários personalizados que consideram tipo de cultivo, clima e época ideal.
            </span>
          </div>
          <div class="mt-5">
            <div>
              <span class="text-subtitle-1">
                Estamos comprometidos com:
              </span>
            </div>
            <div class="mt-2 text-subtitle-1">
              <v-icon 
                class="mr-3"
                color="green"
              >
                mdi-check
              </v-icon>
              <span>Crescer a sustentabilidade da agricultura</span>
            </div>
            <div class="mt-2 text-subtitle-1">
              <v-icon 
                class="mr-3"
                color="green"
              >
                mdi-check
              </v-icon>
              <span>Otimizar o tempo da agricultura</span>
            </div>
            <div class="mt-2 text-subtitle-1">
              <v-icon 
                class="mr-3"
                color="green"
              >
                mdi-check
              </v-icon>
              <span>Melhorar a gestão do campo</span>
            </div>
          </div>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: 'AboutUs',
};
</script>

<style scoped>
</style>
