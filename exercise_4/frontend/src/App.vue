<template>
  <div id="app">
    <!-- Título da aplicação -->
    <h1>Buscar Operadoras</h1>

    <!-- Componente responsável pela interface de busca -->
    <SearchOperators />
  </div>
</template>

<script>
// Importa o componente que contém a funcionalidade principal de busca
import SearchOperators from "./components/SearchOperators.vue";

export default {
  // Registra os componentes que serão usados dentro deste componente principal
  components: {
    SearchOperators,
  },
};
</script>
