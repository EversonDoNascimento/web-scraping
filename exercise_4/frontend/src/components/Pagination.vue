<template>
  <div id="pagination">
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
  props: ["pages", "page"],
  methods: {
    changePage(p) {
      if (p !== this.page) {
        this.$emit("changePage", p);
      }
    },
  },
};
</script>
