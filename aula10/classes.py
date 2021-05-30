class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    def falar(self):
        print(f'{self._nome} esta falando...')

class Cliente(Pessoa):
    def comprar(self):
        print(f'{self._nome} esta comprando...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self._nome} esta estudando...')
