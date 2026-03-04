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
print(f"Total deu R$: {soma}")

#verifica se ta no estoque