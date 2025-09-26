class Livro:
    def __init__(self, titulo, ano, autor, genero, disponivel=True):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__genero = genero
        self.__disponivel = disponivel

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
    
    @disponivel.setter
    def disponivel(self, novo_disponivel):
        self.__disponivel = novo_disponivel

    def livro_dict(self):
        return {
            "titulo": self.titulo,
            "ano": self.ano,
            "autor": self.autor,
            "genero": self.genero,
            "disponivel": self.disponivel
        }
    
    @staticmethod
    def dict_livro(livro):
        """Método que transforma um dicionário em objeto"""
        return Livro(livro["titulo"], livro["ano"], livro["autor"], livro["genero"], livro["disponivel"])