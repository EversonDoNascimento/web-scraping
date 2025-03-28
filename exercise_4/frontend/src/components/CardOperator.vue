<template>
  <table>
    <thead>
      <tr>
        <th>Registro ANS</th>
        <th>CNPJ</th>
        <th>Razão Social</th>
        <th>Nome Fantasia</th>
        <th>Telefone</th>
        <th>Endereço Eletrônico</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="(operadora, index) in operadoras" :key="index">
        <td>{{ operadora.registro_ans }}</td>
        <td>{{ operadora.cnpj }}</td>
        <td>{{ operadora.razao_social || "N/A" }}</td>
        <td>{{ operadora.nome_fantasia || "N/A" }}</td>
        <td>{{ operadora.telefone || "N/A" }}</td>
        <td>{{ operadora.endereco_eletronico || "N/A" }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script>
export default {
  props: ["operadoras"],
};
</script>
