class Cliente:

    def __init__(self, nome: str, fone: str, email: str):
        self.__nome = nome
        self.__fone = fone
        self.__email = email

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
    def fone(self):
        return self.__fone

    @fone.setter
    def fone(self, novo_fone):
        self.__fone = novo_fone

    @fone.getter
    def fone(self):
        return self.__fone
