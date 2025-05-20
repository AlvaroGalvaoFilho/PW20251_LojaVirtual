<<<<<<< HEAD
CREATE_TABLE_CLIENTE="""
=======
CREATE_TABLE_CLIENTE = """
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
CREATE TABLE IF NOT EXISTS Cliente (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    telefone TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    data_nascimento TEXT NOT NULL);
"""

<<<<<<< HEAD
INSERT_CLIENTE="""
INSERT INTO Cliente (nome, cpf, telefone, email, data_nascimento)
VAlUES (?, ?, ?, ?, ?);
"""

UPDATE_CLIENTE="""
UPDATE Cliente 
=======
INSERT_CLIENTE = """
INSERT INTO Cliente (nome, cpf, telefone, email, data_nascimento)
VALUES (?, ?, ?, ?, ?);
"""

UPDATE_CLIENTE = """
UPDATE Cliente
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
SET nome = ?, cpf = ?, telefone = ?, email = ?, data_nascimento = ?
WHERE id = ?;
"""

<<<<<<< HEAD
DELETE_CLIENTE="""
DELETE FROM Cliente 
WHERE id = ?;
"""

GET_CLIENTE_BY_ID="""
=======
DELETE_CLIENTE = """
DELETE FROM Cliente
WHERE id = ?;
"""

GET_CLIENTE_BY_ID = """
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
SELECT id, nome, cpf, telefone, email, data_nascimento
FROM Cliente
WHERE id = ?;
"""

<<<<<<< HEAD
GET_CLIENTES_BY_PAGE="""
=======
GET_CLIENTES_BY_PAGE = """
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
SELECT id, nome, cpf, telefone, email, data_nascimento
FROM Cliente
ORDER BY nome ASC
LIMIT ? OFFSET ?;
"""