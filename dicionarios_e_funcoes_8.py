loja_tech = {
    "unidade": "João Pessoa - PB",
    "status_aberto": True,
    "inventario": {
        "setor_audio": [
            {"id": 101, "nome": "Fone Bluetooth Noise Cancelling", "preco": 850.00, "estoque": 15},
            {"id": 102, "nome": "Caixa de Som à prova d'água", "preco": 420.00, "estoque": 8}
        ],
        "setor_informatica": {
            "perifericos": [
                {"item": "Teclado Mecânico RGB", "marca": "Keychron", "configuracao": "ABNT2"},
                {"item": "Mouse Gamer", "marca": "Logitech", "dpi_max": 16000}
            ],
            "hardwares": {
                "processadores": ["Intel i7", "AMD Ryzen 5", "Apple M3"],
                "gpu": "NVIDIA RTX 4060"
            }
        }
    ,
    "ultimas_vendas": [
        {"data": "2026-03-05", "cliente": "Iury", "total": 1200.50},
        {"data": "2026-03-04", "cliente": "Nathalia", "total": 450.00}
    ]
    }
}

#somando os valores de setor audio
def soma (loja_tech):
    soma = 0
    #tem que caminhar até onde está os valores desejados
    for produto in loja_tech["inventario"]["setor_audio"]:
        soma += produto["preco"]
    return soma

def informatica(loja_tech):
    for produto in loja_tech["inventario"]["setor_informatica"]["perifericos"]:
        print(produto["item"])

def ultimas_vendas(loja_tech):
    soma = 0
    for produto in loja_tech["inventario"]["ultimas_vendas"]:
        soma += produto["total"]
    return soma

#acessando o segundo item do setor audio
segundo = loja_tech["inventario"]["setor_audio"][1]["nome"]
print(segundo)
print("======================")

total = soma(loja_tech)
print(f"total deu R$: {total}")

print("==========================")

#imprimindo os itens do setor de informatica
setor_informatica = informatica(loja_tech)
print(setor_informatica)

print("==========================")
#imprimindo o total das ultimas vendas
vendas = ultimas_vendas(loja_tech)
print(f"Total das ultimas vendas: R$ {vendas}")