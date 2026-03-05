skateshop = {
    "peca_01": {"item": "Shape Maple", "marca": "Santa Cruz", "preco": 450, "quantidade": 5},
    "peca_02": {"item": "Truck Hi", "marca": "Independent", "preco": 380, "quantidade": 2},
    "peca_03": {"item": "Rodinhas", "marca": "Spitfire", "preco": 220, "quantidade": 10},
    "peca_04": {"item": "Rolamentos", "marca": "Bones Red", "preco": 150, "quantidade": 0}
}

#verificador de estoque baixo
def verificar_estoque(skateshop, limite):
    lista_reposicao = [] #lista para os itens
    for peca in skateshop.values():
        if peca.get("quantidade", 0) < limite: #se a quantidade for menor que o limite testado com o .get()
            lista_reposicao.append(peca) #coloque a peca todinha na lista
    return lista_reposicao

verificados = verificar_estoque(skateshop, 10)
print("itens abaixo com menos de 10")
for verificado in verificados:
    print(f"item {verificado["item"]} | qtd: {verificado["quantidade"]}")
