<<<<<<< HEAD
from data.database import obter_conexao
from sql.cliente_sql import *
from models.cliente import Cliente
from datetime import datetime

=======
import datetime
from data.database import obter_conexao
from sql.cliente_sql import *
from models.cliente import Cliente
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9

def criar_tabela_clientes():
    """Cria a tabela Cliente se ela não existir."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(CREATE_TABLE_CLIENTE)
    conexao.commit()
    conexao.close()

def inserir_cliente(cliente: Cliente) -> Cliente:
    """Insere um novo cliente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(INSERT_CLIENTE, 
        (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.data_nascimento))
    cliente.id = cursor.lastrowid
    conexao.commit()
    conexao.close()
    return cliente

def atualizar_cliente(cliente: Cliente) -> bool:
    """Atualiza um cliente existente no banco de dados."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(UPDATE_CLIENTE, 
        (cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.data_nascimento, cliente.id))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def excluir_cliente(id: int) -> bool:
    """Exclui um cliente do banco de dados pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(DELETE_CLIENTE, (id,))
    conexao.commit()
    conexao.close()
    return (cursor.rowcount > 0)

def obter_cliente_por_id(id: int) -> Cliente:
    """Obtém um cliente pelo ID."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_CLIENTE_BY_ID, (id,))
    resultado = cursor.fetchone()
    conexao.close()
    if resultado:
        return Cliente(
            id=resultado[0],
            nome=resultado[1],
            cpf=resultado[2],
            telefone=resultado[3],
<<<<<<< HEAD
            email=resultado[4],
            data_nascimento=datetime.strptime(resultado[5], "%Y-%m-%d").date()
        )
=======
            email=resultado[4],            
            data_nascimento=datetime.datetime.strptime(resultado[5], "%Y-%m-%d").date())
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
    return None

def obter_clientes_por_pagina(limite: int, offset: int) -> list[Cliente]:
    """Obtém uma lista de clientes com paginação."""
    conexao = obter_conexao()
    cursor = conexao.cursor()
    cursor.execute(GET_CLIENTES_BY_PAGE, (limite, offset))
    resultados = cursor.fetchall()
    conexao.close()
    return [Cliente(
        id=resultado[0],
        nome=resultado[1],
        cpf=resultado[2],
        telefone=resultado[3],
        email=resultado[4],
<<<<<<< HEAD
        data_nascimento=datetime.strptime(resultado[5], "%Y-%m-%d").date())
    for resultado in resultados]
=======
        data_nascimento=datetime.datetime.strptime(resultado[5], "%Y-%m-%d").date()
    ) for resultado in resultados]
>>>>>>> 2d8574edd549b6a18f8d475450efcf42a8579ce9
