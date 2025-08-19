from pessoa import Pessoa

p1 = Pessoa('Erick', 30) # p1(objeto) - Foi passado o valor nome(Erick), idade(30)
p2 = Pessoa('Vanessa', 32)


print(p1.get_ano_nascimento()) # Buscando a função dentro da classe, junto com o objeto
print(p2.get_ano_nascimento()) # Buscando a função dentro da classe, junto com o objeto
