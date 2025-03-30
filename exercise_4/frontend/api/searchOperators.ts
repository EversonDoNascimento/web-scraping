import { api } from "./base"; // Instância pré-configurada do Axios para chamadas HTTP
import type { responseOperatorsType } from "./../types/operatorsType"; // Tipagem do retorno da API

// Função responsável por buscar operadoras no backend, com base em:
// - query: termo buscado (nome, CNPJ, etc.)
// - page: página atual da busca
// - per_page: quantidade de resultados por página
export const getOperators = async ({
  query,
  page,
  per_page,
}: {
  query: string;
  page: number;
  per_page: number;
}) => {
  try {
    // Realiza a chamada GET para a rota /search, passando os parâmetros de busca e paginação
    const response: responseOperatorsType = await api.get(
      `/search?query=${query}&page=${page}&per_page=${per_page}`
    );

    // Retorna apenas os dados da resposta (desestruturados do Axios)
    return response.data;
  } catch (error) {
    // Em caso de erro, mostra no console
    console.error(error);
  }
};
