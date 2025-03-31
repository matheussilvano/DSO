from autor import Autor
from capitulo import Capitulo
from editora import Editora

class Livro: 
 
    def __init__(self, codigo: int, titulo: str, ano:int, editora: Editora, autor: Autor, numero_capitulo: Capitulo, titulo_capitulo: Capitulo):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.editora = editora
        self.autor = autor
        self.numero_capitulo = numero_capitulo
        self.titulo_capitulo = titulo_capitulo

    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, novo_codigo):
        self.__codigo = novo_codigo
    
    @codigo.getter
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @titulo.getter
    def titulo(self):
        return self.__titulo

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano):
        self.__ano  = novo_ano

    @ano.getter
    def ano(self):
        return self.__ano

    autores = []
    autores.append(Autor.nome)
    
    def incluir_autor(self, autores):
        if Autor.nome in autores:
            return f'{Autor.nome} já está cadastrado no livro {self.titulo}'
        else:
            autores.append(Autor.nome)
            return f'Autor {Autor.nome} incluído no livro {self.titulo}'

    def excluir_autor(self, autores):
        if Autor.nome in autores:
            autores.remove(Autor.nome)
            return f'Autor {Autor.nome} foi removido da lista de autores de {self.titulo}'
        else:
            return f'O autor {Autor.nome} não está cadastrado na lista de autores de {self.titulo}'

    capitulos = []
    capitulos.append(Capitulo.titulo)

    def incluir_capitulo(self, capitulos):
        ...


    
autor1 = Autor(1, 'Machado de Assis')
autor2 = Autor(2, 'Ariano Suassuna')

editora1 = Editora(1, 'Intrínseca')

capitulo1 = Capitulo(1, 'A volta dos que não foram')
