from classes import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.listar_endereco()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.insere_endereco('Salvador', 'BH')
cliente2.insere_endereco('Rio de Janeiro', 'RJ')
print(cliente2.nome)
cliente2.listar_endereco()
del cliente2
print()

cliente3 = Cliente('Joao', 19)
cliente3.insere_endereco('Sao Paulo', 'SP')
print(cliente3.nome)
cliente3.listar_endereco()
del cliente3
print()
