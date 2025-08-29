from produto import Produto

p1 = Produto('Camisa', 5)
p1.desconto(10)
print(p1.preco)

p2 = Produto('Caneca', 15)
p2.desconto(10)
print(p2.preco)