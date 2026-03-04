from collections import OrderedDict


biblioteca = {
    "game_01": {
        "titulo": "Ori and the Blind Forest",
        "lancamento": 2015,
        "concluido": True,
        "horas_jogadas": 12
    },
    "game_02": {
        "titulo": "Hollow Knight",
        "lancamento": 2017,
        "concluido": False,
        "horas_jogadas": 45
    },
    "game_03": {
        "titulo": "Cyberpunk 2077",
        "lancamento": 2020,
        "concluido": True,
        "horas_jogadas": 80
    },
    "game_04": {
        "titulo": "Elden Ring",
        "lancamento": 2022,
        "concluido": False,
        "horas_jogadas": 120
    }
}

#media de horas jogadas
def media_horas(biblioteca):
    soma_horas = 0
    media_horas = 0
    for jogo in biblioteca.values():
        soma_horas += jogo["horas_jogadas"]
    media_horas = soma_horas/len(biblioteca) 
    return media_horas

horas = media_horas(biblioteca)
print(f"media de horas: {horas}")

#lista apenas com os títulos dos jogos que ainda não foram concluídos
def incompletos(biblioteca):
    lista_incompletos = []
    for jogo in biblioteca.values():
        if jogo["concluido"] == False:
            lista_incompletos.append(jogo["titulo"])
    return lista_incompletos

jogos_incompletos = incompletos(biblioteca) #vai retornar um array
for jogo in jogos_incompletos: #usar o for para percorrer o array
    print(f"Jogo {jogo} incompleto")

#retornar a lista dos jogos mais jogados
def mais_jogados(biblioteca):
    #cria lista vazia manualmente
    lista_jogos = []
    for jogo in biblioteca.values():
        lista_jogos.append(jogo)
    #funcao que serve de etiqueta para as horas    
    def pegar_horas(jogo):
        return jogo["horas_jogadas"]
    
    #ordenamento da lista com base na chave das horas
    lista_jogos.sort(key=pegar_horas, reverse=True)
    return lista_jogos

jogados = mais_jogados(biblioteca)
for jogo in jogados:
    print(f"Título: {jogo['titulo']} | Horas: {jogo['horas_jogadas']}")