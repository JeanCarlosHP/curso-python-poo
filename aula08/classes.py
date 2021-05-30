class CarrinhoDeCompras:
    def __init__(self):
        self._produtos = []

    @property
    def produtos(self):
        return self._produtos

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produtos(self):
        for i in self.produtos:
            print(i.nome, i.valor)

    def soma_total(self):
        total = 0

        for i in self.produtos:
            total += i.valor

        return total


class Produto:
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor

    @property
    def nome(self):
        return self._nome

    @property
    def valor(self):
        return self._valor
