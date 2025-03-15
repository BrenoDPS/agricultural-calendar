<template>
  <v-container id="main-project">
    <v-row>
      <v-divider horizontal class="py-2"></v-divider>
      <v-col cols="12">
        <div class="d-flex justify-center text-h4 font-weight-bold">
          <span>Planeje Sua Plantação</span>
        </div>
      </v-col>

      <!-- Selecione a cidade e a quantidade de mudas -->
      <v-col cols="12" md="6">
        <div class="d-flex justify-center mb-4">
          <h4>Diga a cidade que você deseja fazer sua plantação</h4>
        </div>
        <v-select
          :items="cidades"
          label="Selecione a cidade"
          v-model="cidadeSelecionada"
        ></v-select>
      </v-col>
      <v-col cols="12" md="6">
        <div class="d-flex justify-center mb-4">
          <h4>Diga quantas mudas você irá plantar</h4>
        </div>
        <v-combobox
          :items="quantidades"
          label="Quantidade de mudas"
          v-model="quantidadeSelecionada"
        ></v-combobox>
      </v-col>

      <v-col cols="12">
        <div class="d-flex justify-center">
          <h4>Selecione a Planta que você deseja fazer sua plantação</h4>
        </div>
        <v-row class="justify-space-around mt-3">
          <v-col
            v-for="(planta, index) in plantas"
            :key="index"
            cols="auto"
            @click="selecionarPlanta(planta.nome)"
          >
            <v-card
              :elevation="plantaSelecionada === planta.nome ? 8 : 2"
              :color="plantaSelecionada === planta.nome ? 'rgb(15, 46, 15)' : 'white'"
              class="d-flex flex-column align-center pa-3"
            >
              <v-icon size="40">{{ planta.icone }}</v-icon>
              <p class="text-center">{{ planta.nome }}</p>
            </v-card>
          </v-col>
        </v-row>
      </v-col>

      <v-col cols="12">
        <div class="d-flex justify-center mt-5">
          <v-btn color="rgb(15, 46, 15)" @click="toggleCalendario">
            {{ calendarioVisivel ? 'Ocultar Calendário' : 'Mostrar Calendário' }}
          </v-btn>
        </div>
      </v-col>

      <v-col cols="12" v-if="calendarioVisivel && selectedPlantio">
        <v-card>
          <v-card-title>
            Calendário de Plantio para {{ plantaSelecionada }} em {{ cidadeSelecionada }}
          </v-card-title>
          <v-card-text>
            <v-calendar
              type="month"
              :start="startDate"
              :end="endDate"
              :events="eventosCalendario"
              :weekdays="[0, 1, 2, 3, 4, 5, 6]"
              color="green lighten-4"
              :event-color="getEventColor"
            ></v-calendar>
            <div class="text-subtitle-1 mt-5">
              <span>
                <strong>Dicas de Cultivo:</strong> {{ selectedPlantio.dicas }}
              </span>
            </div>
            <div class="text-subtitle-1">
              <span>
                <strong>Quantidade de Mudas:</strong> {{ quantidadeSelecionada }}
              </span>
            </div>

            <!-- Novo: Selecionar data de plantio -->
            <div class="text-h6 mt-4">
              <span>
                <strong>Selecione a data que você plantou ou deseja plantar:</strong>
              </span>
            </div>
            <v-menu
              ref="menu"
              v-model="menu"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
            >
              <template v-slot:activator="{ props }">
                <v-text-field
                  v-model="dataPlantioUsuario"
                  label="Selecione a data de plantio"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="props"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="dataPlantioUsuario"
                :min="today"
                @click:date="menu = false"
              ></v-date-picker>
            </v-menu>
            <div class="text-subtitle-1 d-flex flex-column align-center">
              <span v-if="dataPlantioUsuario && selectedPlantio" class="text-h5">
                <strong class="font-weight-bold">Você poderá colher entre:</strong>
                {{ formatDate(new Date(dataPlantioUsuario)) }} e {{ formatDate(new Date(selectedPlantio.data_colheita)) }}
              </span>
              <v-btn color="primary" class="mt-5" :disabled="!dataPlantioUsuario" @click="criarColheita">Criar colheita</v-btn>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>

    <v-dialog v-model="dialogVisible" persistent max-width="300px">
      <v-card class="d-flex flex-column align-center">
        <v-card-title class="headline">Lembrete de Evento</v-card-title>
        <v-card-text>{{ dialogMessage }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialogVisible = false">Fechar</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import { useDate } from 'vuetify';
import axios from 'axios';

export default {
  name: 'MainProject',
  data() {
    return {
      cidades: ['Sorocaba', 'Votorantim', 'Ibiuna', 'Itu'],
      quantidades: ['10', '20', '30', '40', '50'],
      cidadeSelecionada: null,
      plantaSelecionada: null,
      quantidadeSelecionada: null,
      calendarioVisivel: false,
      eventosCalendario: [],
      menu: false,
      dataPlantioUsuario: null,
      startDate: null,
      endDate: null,
      today: '',
      // Lista de plantas com ícones
      plantas: [
        { nome: 'Alface', icone: 'mdi-leaf' },
        { nome: 'Rúcula', icone: 'mdi-seed' },
        { nome: 'Couve', icone: 'mdi-sprout' },
        { nome: 'Milho', icone: 'mdi-corn' },
        { nome: 'Melancia', icone: 'mdi-fruit-watermelon' },
        { nome: 'Cenoura', icone: 'mdi-carrot' },
      ],
      plantios: [],
      eventos: [],
      selectedPlantio: null,
      dialogVisible: false,
      dialogMessage: '',
    };
  },
  mounted() {
    const adapter = useDate()
    this.adapter = adapter
    const today = new Date()
    this.today = this.formatDateISO(today)
    this.fetchPlantio()
    this.fetchColheita()
    this.checkEventDates()
  },
  methods: {
    async fetchPlantio() {
      const url = "http://127.0.0.1:8000/api/plantios/";
      try {
        const response = await axios.get(url);
        this.plantios = response.data;
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    },
    async criarColheita() {
      const url = "http://127.0.0.1:8000/api/eventos/";
      const payload = {
        tipo: `Colher ${this.plantaSelecionada}`,
        data: this.formatDateISO(new Date(this.dataPlantioUsuario)),
        quantidade_mudas: this.quantidadeSelecionada
      };
      try {
        await axios.post(url, payload);
        alert('Evento de colheita criado com sucesso!');
      } catch (error) {
        console.error('Erro ao criar o evento de colheita:', error);
      }
    },
    async fetchColheita() {
      const url = "http://127.0.0.1:8000/api/eventos/";
      try {
        const response = await axios.get(url);
        this.eventos = response.data;
      } catch (error) {
        console.error('Erro ao pegar o evento de colheita:', error);
      }
    },
    selecionarPlanta(nome) {
      this.plantaSelecionada = nome;
    },
    toggleCalendario() {
      this.calendarioVisivel = !this.calendarioVisivel;
      if (this.calendarioVisivel) {
        this.mostrarCalendario();
      }
    },
    getPlantaId(nome) {
      const map = {
        'Alface': 1,
        'Rúcula': 2,
        'Couve': 3,
        'Milho': 4,
        'Melancia': 5,
        'Cenoura': 6
      };
      return map[nome] || null;
    },
    getCidadeId(nome) {
      const map = {
        'Sorocaba': 1,
        'Votorantim': 2,
        'Itu': 3,
        'Araçoiaba': 5
      };
      return map[nome] || null;
    },
    mostrarCalendario() {
      if (this.cidadeSelecionada && this.plantaSelecionada && this.quantidadeSelecionada) {
        const cidadeId = this.getCidadeId(this.cidadeSelecionada);
        const bandejaId = this.getPlantaId(this.plantaSelecionada);

        if (!cidadeId || !bandejaId) {
          alert('A cidade ou planta selecionada não está mapeada na API.');
          return;
        }

        const registro = this.plantios.find(item => 
          item.cidade === cidadeId && item.bandeja === bandejaId
        );

        if (!registro) {
          alert('Não há dados de plantio para esta cidade e planta.');
          return;
        }

        this.selectedPlantio = registro;

        const dataInicioPlantio = new Date(registro.data_plantio);
        const dataFimPlantio = new Date(registro.data_colheita);

        let eventosPlantio = [];
        let date = new Date(dataInicioPlantio);
        while (date <= dataFimPlantio) {
          eventosPlantio.push({
            title: 'Bom para plantar',
            start: new Date(date),
            end: new Date(date),
            color: 'green',
            allDay: true,
          });
          date.setDate(date.getDate() + 1);
        }

        this.eventosCalendario = eventosPlantio;
        this.startDate = dataInicioPlantio;
        this.endDate = dataFimPlantio;
        this.calendarioVisivel = true;
      } else {
        alert('Por favor, preencha todos os campos.');
      }
    },
    getEventColor(event) {
      return event.color;
    },
    formatDate(date) {
      return date.toLocaleDateString('pt-BR');
    },
    formatDateISO(date) {
      return date.toISOString().substr(0, 10);
    },
    async checkEventDates() {
      if (this.eventos.length <= 0) {
        setTimeout(this.checkEventDates, 500);
        return;
      }
      const today = new Date().toISOString().substring(0, 10);
      this.eventos.forEach(event => {
        if (event.data === today) {
          this.dialogMessage = event.tipo;
          this.dialogVisible = true;
        }
      });
    }
  },
};
</script>

<style scoped>
.v-card {
  cursor: pointer;
}
.v-card:hover {
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
}
</style>
