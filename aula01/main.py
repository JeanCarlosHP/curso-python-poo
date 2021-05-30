from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('Joao', 32)

p1.falar('POO')
p2.comer('Sorvete')
p1.comer('Churrasco')
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
