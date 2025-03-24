class Aluno:
    
    def __init__(self, nome: str, endereco: str):
        self.__nome = nome
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @nome.getter
    def nome(self):
        return self.__nome

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @endereco.getter
    def endereco(self):
        return self.__endereco

class Professor:

    def __init__(self, nome: str, orientando: Aluno, endereco: str):
        self.nome = nome
        self.orientando = orientando
        self.endereco = endereco

aluno1 = Aluno('Handryos', 'Casa Tal')
professor1 = Professor('Fulano', aluno1, 'Apt tal')

print(professor1.orientando.nome)
print(professor1.orientando.endereco)
