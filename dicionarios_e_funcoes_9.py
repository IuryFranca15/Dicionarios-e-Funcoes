catalogo = {
    "filme_01": {"titulo": "O Labirinto do Fauno", "diretor": "Guillermo del Toro", "nota": 9.2},
    "filme_02": {"titulo": "Interestelar", "diretor": "Christopher Nolan", "nota": 8.7},
    "filme_03": {"titulo": "Blade Runner 2049", "diretor": "Denis Villeneuve"},  # CUIDADO: Sem nota!
    "filme_04": {"titulo": "A Forma da Água", "diretor": "Guillermo del Toro", "nota": 7.3},
    "filme_05": {"titulo": "Filme Misterioso"} # CUIDADO: Sem nota e sem diretor!
}

#pegando os filmes de nota 8 ou mais
def nota_8(catalogo, nota):
    lista = []
    for filme in catalogo.values():
        if filme.get("nota", 0) > nota:
            lista.append(filme)
    return lista

#imprimindo
acima_8 = nota_8(catalogo, 8)
for filme in acima_8:
    print(f"Filme {filme['titulo']} tem nota {filme['nota']}")
