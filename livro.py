class Livro:
    _arquivo = "livro.json"

    def __init__(self, titulo, ano, autor, genero, disponivel=True):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__genero = genero
        self.__disponivel = disponivel