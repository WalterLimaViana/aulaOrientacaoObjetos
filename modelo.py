class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self._nome} - {self.ano} : {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #chamar a class Programa que é uma classe mãe
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.duracao} min : {self._likes} Likes'

class Series(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.temporadas} temporadas : {self._likes} Likes'




vingadores = Filme('Vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()

atlanta = Series('Atlanta', 2018, 2)
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta]
for programa in filmes_e_series:
    #detalhes = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(f'{programa.nome} - {detalhes} D - {programa.likes}')
    # programa.imprime()
    print(programa)

