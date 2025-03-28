export type OperatorsType = {
  nome_fantasia: string;
  registro_ans: string;
  cnpj: string;
  telefone: string;
  endereco_eletronico: string;
  razao_social: string;
};

export type responseOperatorsType = {
  data: {
    page: number;
    pages: number;
    per_page: number;
    results: OperatorsType[];
    total: number;
  };
};
