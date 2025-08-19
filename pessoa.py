# Criando um molde que representa uma pessoa como objeto
# Necessario a criação de uma classe para esse molde

class Pessoa:
    # Quando uma função está dentro de uma classe é chamado de metodo da classe
    def __init__(self, nome, idade, comendo=False, falando=False): # self significa o direcionamento dessa função para o objeto
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    # Definindo status da função comer, mais que 01 vez
    def comer(self, alimento):
        if self.comendo: # Critério pra saber si é a 2 refeição
            print(f'{self.nome} já está comendo {alimento}.')
            return # O código para aqui!

        print(f'{self.nome} está comendo {alimento}.') # Critério pra saber si é a 1 refeição
        self.comendo = True

    # Definindo status da função comer, para PARAR de comer
    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome} parou de comendo.')
        self.comendo = False



