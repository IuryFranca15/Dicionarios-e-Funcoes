setup = {
    "GPU": {"modelo": "RTX 5060", "preco": 2200},
    "CPU": {"modelo": "Ryzen 5 7600", "preco": 1300},
    "RAM": {"modelo": "16GB DDR5", "preco": 600}
}

#calcular o total do setup
def total_a_pagar(setup):
    soma = 0
    for peca in setup.values():
        soma += peca["preco"]
    return soma

total = total_a_pagar(setup)
print(f"Total a pagar R$: {total}")

