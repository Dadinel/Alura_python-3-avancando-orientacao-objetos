class Programa:
    def __init__(self, nome, ano):
        self.__nome = nome.title()
        self.ano = ano
        self.__likes = 0

    def dar_like(self):
        self.__likes += 1

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    # def imprime(self):
    #     print(f'{self.__nome} - {self.ano} - {self.__likes} Likes')

    def __str__(self):
        return f'Nome: {self.__nome} Likes: {self.__likes}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self.programas = programas

    def tamanho(self):
        return len(self.programas)

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes')

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes')

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

vingadores = Filme("vingadores - guerra infinita", 2018, 160)
vingadores.dar_like()

#print(f'{vingadores.nome}: Likes: {vingadores.likes}')

atlanta = Serie("atlanta", 2018, 2)
atlanta.dar_like()
atlanta.dar_like()

#print(f'{atlanta.nome}: Likes: {atlanta.likes}')

filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    #detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas
    print(programa)