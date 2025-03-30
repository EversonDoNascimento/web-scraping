<template>
  <div id="search">
    <div>
      <!-- Campo de busca vinculado à variável 'busca' (Two-way binding com v-model) -->
      <input
        v-model="busca"
        placeholder="Busque por razão social, nome fantasia ou CNPJ"
      />

      <!-- Botão que inicia a busca e reseta para a primeira página -->
      <button @click="searchWithReset">Buscar</button>
    </div>

    <!-- Exibe os resultados apenas se houver algum retorno -->
    <div id="results" v-if="resultado.length">
      <h2 style="width: 100%; text-align: start">
        Total de {{ this.totalResults }} resultados:
      </h2>

      <!-- Componente que renderiza os cards com os dados das operadoras -->
      <CardOperator :operadoras="resultado" />

      <!-- Componente de paginação que permite navegar entre os resultados -->
      <Pagination :page="page" :pages="pages" @changePage="changePage" />
    </div>
  </div>
</template>

<script>
// Importa o componente de cartão que exibe informações de cada operadora
import CardOperator from "./CardOperator.vue";

// Importa a função que faz a requisição à API para buscar operadoras
import { getOperators } from "../../api/searchOperators";

// Importa o componente de paginação
import Pagination from "./Pagination.vue";

export default {
  components: {
    CardOperator,
    Pagination,
  },
  data() {
    return {
      busca: "", // Termo de busca digitado pelo usuário
      resultado: [], // Lista de operadoras retornadas da API
      page: 1, // Página atual
      pages: 0, // Total de páginas
      totalResults: 0, // Total de resultados encontrados
      per_page: 20, // Quantidade de resultados por página
    };
  },
  methods: {
    // Método chamado ao clicar em "Buscar" — reinicia para a página 1
    async searchWithReset() {
      this.page = 1;
      await this.searchOperators();
    },

    // Método que faz a chamada à API com os parâmetros atuais de busca e paginação
    async searchOperators() {
      if (!this.busca) return; // Não faz nada se o campo de busca estiver vazio

      try {
        const search = await getOperators({
          query: this.busca,
          page: this.page,
          per_page: this.per_page,
        });

        // Atualiza os dados da tela com os resultados retornados
        this.resultado = search.results;
        this.totalResults = search.total;
        this.per_page = search.per_page;
        this.page = search.page;
        this.pages = search.pages;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },

    // Atualiza a página atual e faz nova busca
    changePage(page) {
      this.page = page;
      this.searchOperators();
    },
  },
};
</script>
