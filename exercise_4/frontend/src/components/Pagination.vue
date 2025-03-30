<template>
  <div id="pagination">
    <!-- Gera os botões de páginas dinamicamente com base no número total de páginas -->
    <span v-for="(page, index) in pages" key="index">
      <a
        @click.prevent="changePage(page)"
        href="#"
        :style="{ backgroundColor: page === this.page ? 'blue' : '#1a1a1a' }"
      >
        {{ page }}
      </a>
    </span>
  </div>
</template>

<script>
export default {
  // Recebe do componente pai:
  // - 'pages': número total de páginas
  // - 'page': página atual
  props: ["pages", "page"],
  methods: {
    // Emite um evento para o componente pai trocar a página
    changePage(p) {
      if (p !== this.page) {
        this.$emit("changePage", p); // Só emite se a página clicada for diferente da atual
      }
    },
  },
};
</script>
