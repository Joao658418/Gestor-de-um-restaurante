from utils import db_fornecedores


def criar_fornecedor(nif, nome, morada, tel, email, tipo_produto):
    try:
        if not nif or not nome:
            return 400, "NIF e Nome sao obrigatorios."

        if nif in db_fornecedores:
            return 400, "Fornecedor ja existe."

        db_fornecedores[nif] = {
            "nome": nome,
            "morada": morada,
            "telefone": tel,
            "email": email,
            "tipo_produto": tipo_produto
        }
        return 201, db_fornecedores[nif]
    except Exception as e:
        return 500, str(e)


def listar_fornecedores():
    if not db_fornecedores:
        return 404, "Nao existem fornecedores registados."
    return 200, db_fornecedores


def consultar_fornecedor(nif):
    if nif in db_fornecedores:
        return 200, db_fornecedores[nif]
    return 404, "Fornecedor nao encontrado."

def atualizar_fornecedores(nif, novo_nome=nome, novotipo_produto=tipo_produto)
        if nif not in db_fornecedores:
            return 404,  "Cliente não encontrado!"
        fornecedor = {
            "nome": novo_nome,
            "tipo_produto"= novotipo_produto
            "nif": nif
        }
        db_fornecedor[nif].update(fornecedor)
        return 200, fornecedor

    except Exception as e:
        return 400,"Erro interno: {e}"


def atualizar_fornecedor(nif, nome=None, tipo_produto=None):
    if nif not in db_fornecedores:
        return 404, "Fornecedor nao encontrado."
    
    if nome: db_fornecedores[nif]["nome"] = nome
    if tipo_produto: db_fornecedores[nif]["tipo_produto"] = tipo_produto
    
    # Devolve apenas o objeto atualizado
    return 200, db_fornecedores[nif]

def remover_fornecedor(nif):
    if nif in db_fornecedores:
        # Extrai e devolve apenas o objeto removido
        return 200, db_fornecedores.pop(nif)
    return 404, "Fornecedor nao encontrado." = tipo_produto

    

