from sqlalchemy import create_engine, text, URL


def update_venda(engine, id_cliente, id_prato,  quantidade, dia,  hora,  valor):

    query = text("UPDATE venda SET id_cliente = :id_cliente,  id_prato = :id_prato, quantidade = :quantidade, dia = :dia, hora = :hora, valor = :valor WHERE id_cliente = :id_cliente AND id_prato = :id_prato;")
    params = {"id_cliente": id_cliente, "id_prato": id_prato, "quantidade": quantidade, "dia": dia, "hora": hora, "valor": valor}
    
    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def update_usos(engine, id_prato, id_ingrediente):

    query = text("UPDATE usos SET id_prato = :id_prato, id_ingrediente = :id_ingrediente WHERE id_prato = :id_prato AND id_ingrediente = :id_ingrediente ;")
    params = {"id_prato": id_prato, "id_ingrediente": id_ingrediente}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def update_ingrediente(engine, id, nome, data_fabricacao, data_validade, quantidade, observacao):

    query = text("UPDATE ingrediente SET nome = :nome, data_fabricacao = :data_fabricacao, data_validade = :data_validade, quantidade = :quantidade, observacao = :observacao WHERE id = :id;")
    params = {"nome": nome, "data_fabricacao": data_fabricacao, "data_validade": data_validade, "quantidade": quantidade, "observacao": observacao, "id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def update_fornecedor(engine, id, nome, estado_origem):

    query = text("UPDATE fornecedor SET nome = :nome, estado_origem = :estado_origem WHERE id = :id;")
    params = {"nome": nome, "estado_origem": estado_origem, "id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def update_prato(engine, id, nome, descricao, valor, disponibilidade):

    query = text("UPDATE prato SET nome = :nome, descricao = :descricao, valor = :valor, disponibilidade = :disponibilidade WHERE id = :id;")
    params = {"nome": nome, "descricao": descricao, "valor": valor, "disponibilidade": disponibilidade, "id": id }

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def update_cliente(engine, id, nome, sexo, idade, nascimento, pontos):

    query = text("UPDATE cliente SET nome = :nome, sexo = :sexo, idade = :idade, nascimento = :nascimento, pontos = :pontos WHERE id = :id;")
    params = {"nome": nome, "sexo": sexo, "idade": idade, "nascimento": nascimento, "pontos": pontos, "id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def delete_venda(engine, id_cliente, id_prato):

    query = text("DELETE FROM venda WHERE id_cliente = :id_cliente AND id_prato = :id_prato")
    params = {"id_cliente": id_cliente, "id_prato": id_prato }

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()


def delete_usos(engine, id_prato, id_ingrediente):

    query = text("DELETE FROM usos WHERE id_prato = :id_prato AND id_ingrediente = :id_ingrediente")
    params = {"id_prato": id_prato, "id_ingrediente": id_ingrediente}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def delete_ingrediente(engine, id):

    query = text("DELETE FROM ingrediente WHERE id = :id")
    params = {"id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def delete_fornecedor(engine, id):

    query = text("DELETE FROM fornecedor WHERE id = :id")
    params = {"id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def delete_prato(engine, id):

    query = text("DELETE FROM prato WHERE id = :id")
    params = {"id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def delete_cliente(engine, id):

    query = text("DELETE FROM cliente WHERE id = :id")
    params = {"id": id}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def call_function_calcular_pontos(engine, purchase_amount):

    with engine.connect() as connection:
        query = text("SELECT calcular_pontos(:purchase_amount)")
        params = {"purchase_amount": purchase_amount}
        result = connection.execute(query, params)
        calculated_amount = result.fetchall()
        return calculated_amount



def call_procedure_estatisticas(engine):

    with engine.connect() as connection:
        query = text("CALL estatisticas()")
        connection.execute(query)
        connection.commit()


def call_procedure_gastar_pontos(engine, cliente_id: int, prato_id: int):

    with engine.connect() as connection:
        query = text("CALL gastar_pontos(:cliente_id, :prato_id)")
        params = {"cliente_id": cliente_id, "prato_id": prato_id}
        connection.execute(query, params)
        connection.commit()



def call_procedure_reajuste(engine, porcentagem):

    with engine.connect() as connection:
        query = text("CALL reajuste(:porcentagem)")
        params = {"porcentagem": porcentagem}
        connection.execute(query, params)
        connection.commit()


def call_procedure_sorteio(engine):

    with engine.connect() as connection:
        query = text("CALL sorteio()")
        connection.execute(query)
        connection.commit()
    

        
def select_view_ingrediente_mais_usado(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM ingrediente_mais_usado_ultimo_mes")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows
    
def select_view_prato_mais_vendido_mensalmente(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM pratos_mais_vendidos_por_mes")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows

def insert_cliente(engine, nome, sexo, idade, nascimento, pontos):

    query = text("INSERT INTO cliente (nome, sexo, idade, nascimento, pontos) VALUES (:nome, :sexo, :idade, :nascimento, :pontos)")
    params = {"nome": nome, "sexo": sexo, "idade": idade, "nascimento": nascimento, "pontos": pontos}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def select_cliente(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM cliente")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows
    
def insert_prato(engine, nome, descricao, valor, disponibilidade):
    query = text("INSERT INTO prato (nome, descricao, valor, disponibilidade) VALUES (:nome, :descricao, :valor, :disponibilidade)")
    params = {"nome": nome, "descricao": descricao, "valor": valor, "disponibilidade": disponibilidade }

    with engine.connect() as connection:

        connection.execute(query, params)
        connection.commit()

def select_prato(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM prato")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows

def insert_fornecedor(engine, nome, estado_origem):

    query = text("INSERT INTO fornecedor (nome, estado_origem) VALUES (:nome, :estado_origem)")
    params = {"nome": nome, "estado_origem": estado_origem}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def select_fornecedor(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM fornecedor")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows
    
def insert_ingrediente(engine, nome, data_fabricacao, data_validade, quantidade, observacao):

    query = text("INSERT INTO ingrediente (nome, data_fabricacao, data_validade, quantidade, observacao) VALUES (:nome, :data_fabricacao, :data_validade, :quantidade, :observacao)")
    params = {"nome": nome, "data_fabricacao": data_fabricacao, "data_validade": data_validade, "quantidade": quantidade, "observacao": observacao}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def select_ingrediente(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM ingrediente")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows

def insert_usos(engine, id_prato, id_ingrediente):

    query = text("INSERT INTO usos (id_prato, id_ingrediente) VALUES (:id_prato, :id_ingrediente)")
    params = {"id_prato": id_prato, "id_ingrediente": id_ingrediente}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def select_usos(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM usos")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows


def insert_venda(engine, id_cliente, id_prato, quantidade, dia, hora, valor):

    query = text("INSERT INTO venda (id_cliente, id_prato, quantidade, dia, hora, valor) VALUES (:id_cliente, :id_prato, :quantidade, :dia, :hora, :valor)")
    params = {"id_cliente": id_cliente, "id_prato": id_prato, "quantidade": quantidade, "dia": dia, "hora": hora, "valor": valor}

    with engine.connect() as connection:

            connection.execute(query, params)
            connection.commit()

def select_venda(engine):

    with engine.connect() as connection:
            query = text("SELECT * FROM venda")
            result = connection.execute(query)
            rows = result.fetchall()
            return rows