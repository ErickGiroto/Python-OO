# Criando um molde que representa uma pessoa como objeto
# Necessario a criação de uma classe para esse molde

class Pessoa:
    # Quando uma função está dentro de uma classe é chamado de metodo da classe
    def __init__(self, nome, idade, comendo=False, falando=False): # self significa o direcionamento dessa função para o objeto
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Definindo status da função comer
    def comer(self, alimento):
        print(f'{self.nome} está comendo {alimento}.') # Passado o elemento {alimento}
        self.comendo = True


