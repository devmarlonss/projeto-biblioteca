from usuario import Usuario
from livro import Livro
from dados import Dados

class Biblioteca:
    _arquivo = "biblioteca"

    def __init__(self):
        self.usuarios = []
        self.livros = []

    def remover_usuario(self, cpf):
        for u in self.usuarios:
            if u.cpf == cpf:
                self.usuarios.remove(u)
                return True
        return False

    def buscar_usuario(self, cpf, show=True):
        for u in self.usuarios:
            if u.cpf == cpf:
                if (show):
                    return (u.nome, u.cpf)
                return True
        return False

    def exibir_usuarios(self):
        for u in self.usuarios:
            print(f"Nome: {u.nome}\nCPF: {u.cpf}\n")

    @staticmethod
    def verificar_cpf(cpf):
        """"Verifica se o CPF é válido"""
        return (cpf.isdigit() and len(cpf) == 11)