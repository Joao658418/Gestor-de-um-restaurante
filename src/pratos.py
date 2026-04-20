from utils import db_pratos


def criar_prato(nome, preco, estrelas, tipo, ingredientes):
    try:
        if not nome or not preco:
            return 400, "Nome e Preço são obrigatórios."

        # Gerar ID automático simples
        novo_id = str(len(db_pratos) + 1)

        novo_prato = {
            "id": novo_id,
            "nome": nome,
            "preco": preco,
            "estrelas": estrelas,
            "tipo": tipo,
            "ingredientes": ingredientes
        }
        db_pratos.append(novo_prato)
        return 201, "Prato criado com sucesso."
    except Exception as e:
        return 500, str(e)


def listar_pratos():
    if not db_pratos:
        return 404, "Não existem pratos no cardápio."

    print("\n--- CARDÁPIO ---")
    for p in db_pratos:
        print(f"ID: {p['id']} | Nome: {p['nome']} | Preço: {p['preco']}€ | Tipo: {p['tipo']}")
    return 200, "Sucesso"


def consultar_prato(id_prato):
    for p in db_pratos:
        if p["id"] == id_prato:
            print(f"\n🔍 Detalhes: {p}")
            return 200, "Sucesso"
    return 404, "Prato não encontrado."


def atualizar_prato(id_prato, nome=None, preco=None, estrelas=None, tipo=None, ingredientes=None):
    for p in db_pratos:
        if p["id"] == id_prato:
            if nome: p["nome"] = nome
            if preco: p["preco"] = preco
            if estrelas: p["estrelas"] = estrelas
            if tipo: p["tipo"] = tipo
            if ingredientes: p["ingredientes"] = ingredientes
            return 200, "Atualizado"
    return 404, "Prato não encontrado."


def remover_prato(id_prato):
    for i, p in enumerate(db_pratos):
        if p["id"] == id_prato:
            db_pratos.pop(i)
            return 200, "Removido"
    return 404, "Prato não encontrado."
