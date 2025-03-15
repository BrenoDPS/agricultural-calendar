<template>
  <v-container id="contact-us">
    <!-- Imagem de capa -->
    <v-img
      class=""
      width="2000"
      height="500px"
      aspect-ratio="16/9"
      cover
      src="https://img.freepik.com/fotos-gratis/foto-aerea-de-um-lindo-campo-verde-agricola-perto-de-montanhas_181624-40867.jpg?t=st=1731608599~exp=1731612199~hmac=d4b426619c3a485b4c8f29a40b014203d3522b754c80f8308d58f6e2aa750591&w=2000"
    ></v-img>

    <!-- Seção de Notícias com v-slide-group -->
    <v-sheet class="mx-auto mt-6" elevation="8" max-width="1800" height="650" style="background-color: rgb(15, 46, 15);">
      <v-slide-group
        v-model="model"
        class="pa-4"
        selected-class="bg-success"
        show-arrows
      >
        <v-slide-group-item
          v-for="(noticia, index) in noticias"
          :key="index"
          v-slot="{ isSelected, toggle, selectedClass }"
        >
          <v-card
            :class="['ma-4']"
            color=""
            height="590"
            width="500"
            @click="toggle"
          >
            <v-img :src="noticia.imgUrl" height="450px" cover></v-img>
            <v-card-title class="text-center text-h6">{{ noticia.titulo }}</v-card-title>
            <v-card-actions>
              <v-btn
                :href="noticia.url"
                target="_blank"
                color="primary"
                text
              >
                Leia Mais
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-slide-group-item>
      </v-slide-group>
    </v-sheet>

    <!-- Formulário de Contato -->
    
  </v-container>

  <v-snackbar
    v-model="dialog"
    :timeout="4000"
  >
    <v-card>
      <v-card-title>
        Email enviado com sucesso.
      </v-card-title>
    </v-card>
  </v-snackbar>
</template>

<script>
import emailjs from 'emailjs-com';
import axios from 'axios';

export default {
  name: 'ContactUs',
  data() {
    return {
      nome: '',
      titulo: '',
      mensagem: '',
      dialog: false,
      model: 0, // Para o controle do slide group
      noticias: [
        // {
        //   url: 'https://www.canalrural.com.br/tempo/frente-fria-traz-temporais-e-risco-de-geada-veja-quando-e-onde/',
        //   title: 'Frente fria traz temporais e risco de geada; veja quando e onde',
        //   imgUrl: 'https://imagens-cdn.canalrural.com.br/wp-content/uploads/IMG-20200715-WA0052.jpg',
        // },
        // {
        //   url: 'https://www.canalrural.com.br/agricultura/projeto-soja-brasil/soja-confira-a-projecao-da-conab-para-a-safra-brasileira-24-25/',
        //   title: 'Soja: confira a projeção da Conab para a safra brasileira 24/25',
        //   imgUrl: 'https://imagens-cdn.canalrural.com.br/2024/10/FOTOPARANA.png',
        // },
        // {
        //   url: 'https://www.canalrural.com.br/noticias-trilha-da-soja/produtores-de-soja-se-preparam-para-o-clima-desfavoravel/',
        //   title: 'Com uso de tecnologias, sojicultor fica mais preparado para enfrentar adversidades climáticas no Brasil',
        //   imgUrl: 'https://imagens-cdn.canalrural.com.br/2024/01/6_Lado-esquerdo-material-sentindo-seca-e-calor.jpeg',
        // },
        // {
        //   url: 'https://www.canalrural.com.br/agricultura/conab-mantem-previsao-de-safra-recorde-de-graos-no-rio-grande-do-sul-para-2024-2025/',
        //   title: 'Conab mantém previsão de safra recorde de grãos no Rio Grande do Sul para 2024/2025',
        //   imgUrl: 'https://imagens-cdn.canalrural.com.br/2024/08/08-2024-graos.jpg',
        // },
        // {
        //   url: 'https://www.canalrural.com.br/agricultura/soja-milho-arroz-e-feijao-veja-as-condicoes-e-as-estimativas-de-produtividade/',
        //   title: 'Soja, milho, arroz e feijão: veja as condições e as estimativas de produtividade',
        //   imgUrl: 'https://imagens-cdn.canalrural.com.br/2024/11/1731014049790467.jpg',
        // },
      ],
    };
  },
  mounted() {
    this.fetchNoticias()
  },
  methods: {
    async fetchNoticias() {
      const url = "http://127.0.0.1:8000/api/notificacoes/";
      try {
        const response = await axios.get(url);
        this.noticias = response.data;
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    },
    enviarEmail() {
      if (this.nome && this.titulo && this.mensagem) {
        // const templateParams = {
        //   from_name: this.nome,
        //   subject: this.titulo,
        //   message_html: this.mensagem,
        // };

        // emailjs
        //   .send(
        //     'service_m7rhlbe', // Substitua pelo seu Service ID do EmailJS
        //     'SEU_TEMPLATE_ID', // Substitua pelo seu Template ID do EmailJS
        //     templateParams,
        //     'SEU_USER_ID' // Substitua pelo seu User ID do EmailJS
        //   )
        //   .then(
        //     (response) => {
        //       alert('Email enviado com sucesso!');
        //       this.nome = '';
        //       this.titulo = '';
        //       this.mensagem = '';
        //     },
        //     (error) => {
        //       alert('Ocorreu um erro ao enviar o email:', error);
        //     }
        //   );
        this.dialog = true
      } else {
        alert('Por favor, preencha todos os campos.');
      }
    },
  },
};
</script>

<style scoped>
/* Ajuste para alinhar a altura do card e o conteúdo da imagem */
.v-card .v-img {
  object-fit: cover;
}
</style>
