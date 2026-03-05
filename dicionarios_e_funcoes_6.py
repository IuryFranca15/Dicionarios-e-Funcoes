setup = {
    "monitor": {
        "modelo": "Samsung Odyssey G7",
        "especificacoes": "27 polegadas, 240Hz, QHD",
        "preco": 2800,
        "em_estoque": True
    },
    "gpu": {
        "modelo": "RTX 5060",
        "vram": "12GB GDDR7",
        "preco": 2200,
        "em_estoque": False

    },
}

#soma precos
def soma_precos(setup):
    soma = 0
    for item in setup.values():
        soma += item["preco"]
    return soma

soma = soma_precos(setup)
print(f"Total R$: {soma}")

#verifica se ta no estoque
def verifica_estoque(setup):
    lista_faltando = []
    #aqui o pulo do gato para adicionar identificar a chave e adicionar numa lista
    for chave, conteudo in setup.items():
        if conteudo["em_estoque"] == False:
            lista_faltando.append(chave)
    return lista_faltando

faltando = verifica_estoque(setup)
for falta in faltando:
    print(f"itens faltando: {falta}")
