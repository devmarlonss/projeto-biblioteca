from usuario import Usuario
from livro import Livro
from dados import Dados

class Biblioteca:
    _arquivo = "biblioteca"

    def __init__(self):
        self.usuarios = []
        self.livros = []

    def adicionar_usuario(self, nome, cpf, senha):
        if (self.verificar_cpf(cpf)):
            if (not self.buscar_usuario(cpf, show=False)):
                self.usuarios.append(Usuario(nome, cpf, senha))
                return True
            return "USUÁRIO JÁ CADASTRADO!"
        return "CPF INVÁLIDO!"

    def remover_usuario(self, cpf):
        for u in self.usuarios:
            if (u.cpf == cpf):
                self.usuarios.remove(u)
                return True
        return False

    def buscar_usuario(self, cpf, show=True):
        for u in self.usuarios:
            if (u.cpf == cpf):
                if (show):
                    return (u.nome, u.cpf)
                return True
        return False

    def exibir_usuarios(self):
        for u in self.usuarios:
            print(f"Nome: {u.nome}\nCPF: {u.cpf}\n")

    def adicionar_livro(self, titulo, autor, ano, genero):
        if (not self.buscar_livro(titulo, show=False)):
            livro = Livro(titulo, ano, autor, genero)
            self.livros.append(livro)
            return True
        return "LIVRO JÁ CADASTRADO!"

    def remover_livro(self, titulo):
        for l in self.livros:
            if (l.titulo == titulo):
                self.livros.remove(l)
                return True
        return False

    def buscar_livro(self, titulo, show=True):
        for l in self.livros:
            if (l.titulo == titulo):
                if (show):
                    return (l.titulo, l.autor, l.ano, l.genero, l.disponivel)
                return True
        return False
    
    def exibir_livros(self):
        if (self.livros):
            for l in self.livros:
                print(f"Título: {l.titulo} | Autor: {l.autor} | Ano: {l.ano} | Gênero: {l.genero} | Disponível: {"Sim" if l.disponivel else "Não"}")
        print("\n Nenhum livro cadastrado!")

    @staticmethod
    def verificar_cpf(cpf):
        """"Verifica se o CPF é válido"""
        return (cpf.isdigit() and len(cpf) == 11)