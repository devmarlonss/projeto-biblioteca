from usuario import Usuario
from livro import Livro
from dados import Dados

class Biblioteca:
    _arquivo = "biblioteca"

    def __init__(self):
        self.usuarios = []
        self.livros = []