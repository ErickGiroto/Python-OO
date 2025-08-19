from pessoa import Pessoa

p1 = Pessoa('Erick', 30) # p1(objeto) - Foi passado o valor nome(Erick), idade(30)

# Solicitei que a pessoa iniciasse á comer!
p1.comer('maçã') # Foi passado o valor do alimento(Maça)
# Solicitei que a pessoa parasse de comer!
p1.para_comer()

print('-----------------')
# Solicitei novamente a pessoa que iniciasse á comer!
p1.comer('maçã') # Foi passado o valor do alimento(Maça)
# Solicitei que a pessoa parasse de comer!
p1.para_comer()
# Solicitei que a pessoa parasse de comer novamente!
p1.para_comer()