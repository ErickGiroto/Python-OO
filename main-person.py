from pessoa import Pessoa

# Realizando metodos de classes
p1 = Pessoa.por_ano_nascimento('Erick', 1995) # Opção 01
p1 = Pessoa('Erick', 1995) # Opção 02
print(p1)

print(p1.nome, p1.idade, 'anos')

print(Pessoa.gera_id()) # Gerando pelo class
print(p1.gera_id()) # Gerando

