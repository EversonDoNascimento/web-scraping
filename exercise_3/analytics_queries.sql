-- Query 1: Top 10 operadoras com maiores despesas no último trimestre 


SELECT 
    o.razao_social,
    SUM(dc.saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras o ON dc.registro_ans = o.registro_ans
WHERE 
    (dc.descricao LIKE '%SINISTROS CONHECIDOS%' OR dc.descricao LIKE '%AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%' OR dc.descricao LIKE '%EVENTOS%')
    AND dc.data BETWEEN '2024-07-01' AND '2024-10-01'
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;


-- Query 2: Top 10 operadoras com maiores despesas no último ano

SELECT 
    o.razao_social,
    SUM(dc.saldo_final) AS total_despesas
FROM 
    demonstracoes_contabeis dc
JOIN 
    operadoras o ON dc.registro_ans = o.registro_ans
WHERE 
    (dc.descricao LIKE '%SINISTROS CONHECIDOS%' OR dc.descricao LIKE '%AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%' OR dc.descricao LIKE '%EVENTOS%')
    AND dc.data BETWEEN '2023-10-01' AND '2024-10-01'
GROUP BY 
    o.razao_social
ORDER BY 
    total_despesas DESC
LIMIT 10;