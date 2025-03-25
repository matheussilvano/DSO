class Endereco:
    
    def __init__(self, cidade: str, estado:str):
        self.__cidade = cidade
        self.__estado = estado

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, nova_cidade):
        self.__cidade = nova_cidade

    @cidade.getter
    def cidade(self):
        return self.__cidade

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, novo_estado):
        self.__estado = novo_estado
    
    @estado.getter
    def estado(self):
        return self.__estado

class Aluno:

    def __init__(self, nome: str, endereco: Endereco):
        self.nome = nome
        self.endereco = endereco

class Professor:

    def __init__(self, nome: str, orientando: Aluno, endereco: Endereco):
        self.nome = nome
        self.orientando = orientando
        self.endereco = endereco

endereco1 = Endereco('Floripa', 'SC')
aluno1 = Aluno('Handryos', endereco1)
print(f'Cidade: {aluno1.endereco.cidade}, Estado: {aluno1.endereco.estado}')
