<template>
  <div id="search">
    <div>
      <input
        v-model="busca"
        placeholder="Busque por razão social, nome fantasia ou CNPJ"
      />
      <button @click="searchWithReset">Buscar</button>
    </div>

    <div id="results" v-if="resultado.length">
      <h2 style="width: 100%; text-align: start">
        Total de {{ this.totalResults }} resultados:
      </h2>
      <CardOperator :operadoras="resultado" />
      <Pagination :page="page" :pages="pages" @changePage="changePage" />
    </div>
  </div>
</template>

<script>
import CardOperator from "./CardOperator.vue";
import { getOperators } from "../../api/searchOperators";
import Pagination from "./Pagination.vue";

export default {
  components: {
    CardOperator,
    Pagination,
  },
  data() {
    return {
      busca: "",
      resultado: [],
      page: 1,
      pages: 0,
      totalResults: 0,
      per_page: 20,
    };
  },
  methods: {
    async searchWithReset() {
      this.page = 1;
      await this.searchOperators();
    },
    async searchOperators() {
      if (!this.busca) return;
      try {
        const search = await getOperators({
          query: this.busca,
          page: this.page,
          per_page: this.per_page,
        });

        this.resultado = search.results;
        this.totalResults = search.total;
        this.per_page = search.per_page;
        this.page = search.page;
        this.pages = search.pages;
      } catch (error) {
        console.error("Erro ao buscar operadoras:", error);
      }
    },

    changePage(page) {
      this.page = page;
      this.searchOperators();
    },
  },
};
</script>
