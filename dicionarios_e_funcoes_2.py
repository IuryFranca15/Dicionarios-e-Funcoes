
albuns = {
    "album 1": {
        "titulo": "is this it",
        "artista": "The Strokes",
        "ano": 2001,
        "genero": "Indie Rock"
    },
    "album 2": {
        "titulo": "whatever people say i am...",
        "artista": "Arctic Monkeys",
        "ano": 2006,
        "genero": "Indie Rock"
    },
    "album 3": {
        "titulo": "el camino",
        "artista": "The Black Keys",
        "ano": 2011,
        "genero": "Blues Rock"
    },
    "album 4": {
        "titulo": "...like clockwork",
        "artista": "Queens of the Stone Age",
        "ano": 2013,
        "genero": "Stoner Rock"
    },
    "album 5": {
        "titulo": "pinkerton",
        "artista": "Weezer",
        "ano": 1996,
        "genero": "Power Pop"
    }
}

#pesquisar albuns por genero
def filtra_genero(albuns, genero_pesquisado): #passa o dicionario e a var pesquisada
    lista = [] #cria uma lista pra armazenar os titulos
    for album in albuns.values():
        if album["genero"].lower() == genero_pesquisado: #se o genero corresponder
            lista.append(album["titulo"]) #adiciona o titulo na lista
    if lista:
        return lista
    else:
        return "Não encontrados álbuns desse gênero"

#imprimir os albuns depois de depois dos anos 2000
def filtra_ano(albuns, ano = 2000):
    lista = []
    for album in albuns.values():
        if album["ano"] >= ano:
            lista.append(album["titulo"])
    if lista:
        return lista
    else:
        return

genero_pesquisado = input("informe um genero: \n").lower()
pesquisa = filtra_genero(albuns, genero_pesquisado)

#imprimindo
print(f"genero escolhido: {genero_pesquisado}")

for nome in pesquisa:
    print(f"título: {nome}")

#imprimindo
filtro_ano = filtra_ano(albuns, ano = 2000)
print("imprimindo os titulos depois de 2000")
for nome in filtro_ano:
    print(f"titulo: {nome}")

