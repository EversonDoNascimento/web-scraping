<template>
  <div id="app">
    <h1>Buscar Operadoras</h1>
    <SearchOperators />
  </div>
</template>

<script>
import SearchOperators from "./components/SearchOperators.vue";
import { getOperators } from "./../api/searchOperators";

export default {
  components: {
    SearchOperators,
  },
};
</script>
