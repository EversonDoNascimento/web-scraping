DROP TABLE IF EXISTS demonstracoes_contabeis;


CREATE TABLE demonstracoes_contabeis (
    id INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    registro_ans INT,
    codigo_conta VARCHAR(20),
    descricao VARCHAR(255),
    saldo_inicial DECIMAL(15,2),
    saldo_final DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);
