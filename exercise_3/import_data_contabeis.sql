LOAD DATA LOCAL INFILE './../data/last_2_years/2024/1T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2024/2T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2024/3T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2024/4T2024.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2023/1T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2023/2T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2023/3T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%Y-%m-%d'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');

LOAD DATA LOCAL INFILE './../data/last_2_years/2023/4T2023.csv'
INTO TABLE demonstracoes_contabeis
CHARACTER SET utf8mb4
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@data, @reg_ans, @cod_conta, @descricao, @saldo_ini, @saldo_fim)
SET
    data = STR_TO_DATE(@data, '%d/%m/%Y'),
    registro_ans = @reg_ans,
    codigo_conta = @cod_conta,
    descricao = @descricao,
    saldo_inicial = REPLACE(@saldo_ini, ',', '.'),
    saldo_final = REPLACE(@saldo_fim, ',', '.');
