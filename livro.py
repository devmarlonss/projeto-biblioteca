class Livro:
    def __init__(self, titulo, ano, autor, genero):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__genero = genero
        self.__disponivel = True

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @property
    def autor(self):
        return self.__autor
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def disponivel(self):
        return self.__disponivel
    
    def alterar_disponibilidade(self):
        self.disponivel = not self.disponivel
