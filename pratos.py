from utils import db_pratos


def adicionar_prato(nome, preco, estrelas, tipo, ingredientes_str):
    # Transformar string em SET para ingredientes únicos
    ing_set = set([i.strip() for i in ingredientes_str.split(",")])

    novo_prato = {
        "id": len(db_pratos) + 1,
        "nome": nome,
        "preco": preco,
        "estrelas": estrelas,
        "tipo": tipo,
        "ingredientes": ing_set
    }
    db_pratos.append(novo_prato)
    print(f"Prato '{nome}' cadastrado!")


def atualizar_prato(id_procurado, nome, preco, estrelas, tipo, ingredientes_str):
    for prato in db_pratos:
        if prato["id"] == id_procurado:
            prato["nome"] = nome
            prato["preco"] = preco
            prato["estrelas"] = estrelas
            prato["tipo"] = tipo
            prato["ingredientes"] = set([i.strip() for i in ingredientes_str.split(",")])
            print(f"Prato ID {id_procurado} atualizado!")
            return
    print("ID de prato não encontrado.")
