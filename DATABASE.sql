--Tabela cliente pedido:

-- CREATE TABLE cliente (
--     cd_Cliente INTEGER
--     Nm_Cliente VARCHAR(50)
-- );

-- CREATE TABLE pedido (
--     Nr_Pedido INTEGER
--     cd_Cliente INTEGER
--     dt_Pedido DATE
-- );

CREATE TABLE produto (
    Cd_Produto INTEGER NOT NULL PRIMARY KEY,
    Ds_Produtos VARCHAR(50) NOT NULL,
    preco DECIMAL(5,2) NOT NULL
)

CREATE TABLE pedido (
    Nr_Pedido INTEGER NOT NULL PRIMARY KEY FOREIGN KEY
    Cd_Produto INTEGER NOT NULL PRIMARY KEY FOREIGN KEY,
    Quantidade INTEGER NOT NULL,
    Preco DECIMAL(5,2) NOT NULL;
)


