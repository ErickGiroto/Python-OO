from pessoa import Pessoa

# Tem que instanciar cada objeto vindo do mesmo molde
p1 = Pessoa() # p1 é o objeto
p2 = Pessoa() # p2 é o objeto

#p1 não é igual p2, veja o print abaixo
print("p1: ", p1) # objeto
print("p2: ", p2) # objeto

p1.nome = 'Erick'
p2.nome = 'Joey'

print(p1.nome) # As variavéis, são atributos(nome) da classe(p1)
print(p2.nome)