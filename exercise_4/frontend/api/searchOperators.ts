import { api } from "./base";
import type { responseOperatorsType } from "./../types/operatorsType";
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
    const response: responseOperatorsType = await api.get(
      `/search?query=${query}&page=${page}&per_page=${per_page}`
    );
    return response.data;
  } catch (error) {
    console.error(error);
  }
};
