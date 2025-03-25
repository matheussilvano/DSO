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

    def __init__(self, nome: str, orientando: Aluno, endereco: Endereco):
        self.__nome = nome
        self.__orientando = orientando
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
    def orientando(self):
        return self.__orientando

    @orientando.setter
    def orientando(self, novo_orientando):
        self.__orientando = novo_orientando

    @orientando.getter
    def orientando(self):
        return self.__orientando
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, novo_endereco):
        self.__endereco = novo_endereco

    @endereco.getter
    def endereco(self):
        return self.__endereco

endereco1 = Endereco('Floripa', 'SC')
aluno1 = Aluno('Handryos', endereco1)
print(f'Cidade: {aluno1.endereco.cidade}, Estado: {aluno1.endereco.estado}')
