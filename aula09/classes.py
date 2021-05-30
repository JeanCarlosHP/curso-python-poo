class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._enderecos = []

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade

    def insere_endereco(self, cidade, estado):
        self._enderecos.append(Endereco(cidade, estado))

    def listar_endereco(self):
        for i in self._enderecos:
            print(i.cidade, i.estado)
    
    def __del__(self):
        print(f'{self._nome} foi apagado.')


class Endereco:
    def __init__(self, cidade, estado):
        self._cidade = cidade
        self._estado = estado

    @property
    def cidade(self):
        return self._cidade

    @property
    def estado(self):
        return self._estado

    def __del__(self):
        print(f'{self._cidade} foi apagado.')