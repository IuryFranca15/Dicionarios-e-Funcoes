biblioteca_streaming = {
    "usuario": "Iury",
    "assinatura": "Premium",
    "categorias": {
        "ficcao_cientifica": [
            {"id": 1, "titulo": "Children of Men", "detalhes": {"diretor": "Alfonso Cuarón", "imdb": 7.9}},
            {"id": 2, "titulo": "Arrival", "detalhes": {"diretor": "Denis Villeneuve", "imdb": 7.9}}
        ],
        "terror_psicologico": [
            {"id": 3, "titulo": "The Lighthouse", "detalhes": {"diretor": "Robert Eggers", "imdb": 7.4}},
            {"id": 4, "titulo": "Hereditary", "detalhes": {"diretor": "Ari Aster"}} # Nota IMDB faltando!
        ],
        "animacao": [
            {"id": 5, "titulo": "Pinocchio", "detalhes": {"diretor": "Guillermo del Toro", "imdb": 7.6}}
        ]
    },
    "recomendados_hoje": ["Arrival", "Pinocchio", "The Lighthouse"]
}

#Crie uma função que retorne uma string formatada com os dados principais do usuário.

def dados(biblioteca_streaming):
    usuario = biblioteca_streaming.get("usuario")
    assinatura = biblioteca_streaming.get("assinatura")
    recomendados_hoje = biblioteca_streaming.get("recomendados_hoje")
    
    return usuario, assinatura, recomendados_hoje

dados = dados(biblioteca_streaming)
for dado in dados.items():
    print(f"{dado}")















#Acesse a lista de filmes da categoria "ficcao_cientifica".
#Quando encontrar o filme com o título "Arrival", extraia a nota dele dentro de detalhes.
def encontrar_filme(biblioteca_streaming):
    lista = [] #criando a lista para armazenar os detalhes
    for filme in biblioteca_streaming["categorias"]["ficcao_cientifica"]: #acessando onde o filme está
        if filme.get("titulo", "não encontrado") == "Arrival": #encontrando o filme
            lista.append(filme["detalhes"]) #dando append nos detalhes do filme
    return lista

detalhe_filme = encontrar_filme(biblioteca_streaming)

for detalhes in detalhe_filme: #para cada detalhe do filme
    for chave, valor in detalhes.items(): #para a chave e o valor dos itens
        print(f"{chave}: {valor}") #imprimir a chave e o valor





