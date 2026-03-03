

skate_pecas = {
    "shape": 250.00,
    "truck": 180.00,
    "rodinha": 120.00,
    "rolamento": 80.00,
    "lixa": 45.00
}

def calcular_combo(skate_pecas, item1, item2): #passa o dic, e os 2 itens
    if item1 in skate_pecas and item2 in skate_pecas:
        combo = skate_pecas[item1] + skate_pecas[item2] #acessa o valor assim
        return f"Combo de {item1} e {item2} com 15% OFF: R$ {combo:.2f}"
    else:
        return f"Algum dos itens não está na lista"

item1 = input("qual a primeira peca? \n").lower()
item2 = input("qual a segunda peca? \n").lower()

resultado = calcular_combo(skate_pecas, item1, item2)
print(resultado)