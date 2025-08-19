from pessoa import Pessoa

p1 = Pessoa('Erick', 30) # p1(objeto) - Foi passado o valor nome(Erick), idade(30)
p2 = Pessoa('Vanessa', 32)


print(p1.ano_atual)
print(p2.ano_atual) # Usando á variavel da instancia
print(Pessoa.ano_atual) # Usuando a classe em si
