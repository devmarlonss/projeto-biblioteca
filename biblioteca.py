from usuario import Usuario
from livro import Livro
from dados import Dados

class Biblioteca:
    _arquivo = "biblioteca"

    def __init__(self):
        self.usuarios = []
        self.livros = []

    def exibir_usuarios(self):
        for u in self.usuarios:
            print(f"Nome: {u.nome}\nCPF: {u.cpf}\n")

    @staticmethod
    def verificar_cpf(cpf):
        """"Verifica se o CPF é válido"""
        return (cpf.isdigit() and len(cpf) == 11)