// Define a estrutura dos dados de uma operadora retornada pela API
export type OperatorsType = {
  nome_fantasia: string; // Nome público da operadora
  registro_ans: string; // Registro oficial na ANS
  cnpj: string; // CNPJ da empresa
  telefone: string; // Telefone de contato
  endereco_eletronico: string; // E-mail ou outro meio eletrônico
  razao_social: string; // Nome jurídico da empresa
};

// Define o formato da resposta completa da API de busca de operadoras
export type responseOperatorsType = {
  data: {
    page: number; // Página atual
    pages: number; // Total de páginas disponíveis
    per_page: number; // Quantidade de resultados por página
    results: OperatorsType[]; // Lista de operadoras encontradas
    total: number; // Total de resultados retornados
  };
};
