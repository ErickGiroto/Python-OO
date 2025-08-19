# Importando a biblioteca data
from datetime import datetime
from random import randint

# Criando um molde que representa uma pessoa como objeto
# Necessary a criação de uma classe para esse molde

class Pessoa:
    # Definindo uma variable data da classe Pessoa
    # Essa variable será acessada por todas as funções dessa classe.
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))


    # Quando uma função está numa classe é chamado de methods da classe
    def __init__(self, nome, idade, comendo=False, falando=False): # self significa o direcionamento dessa função para o objeto
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando


    # Manipulação com á variable falando! ---------------------------------------
    # Checando si a pessoa está a comer para poder falar!
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar está comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando sobre {assunto}.')
            return

        print(f'{self.nome} está falando sobre {assunto}.')
        self.falando = True

    # Manipulação com á variable falando! ---------------------------------------
    # Fazer a pessoa parar de falar!
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando.')
            return

        print(f'{self.nome} parou de falar!')
        self.falando = False

    # Manipulação com á variable comendo! ---------------------------------------
    # Definindo status da função comer, mais que 01 vez
    def comer(self, alimento):
        if self.comendo: # Critério pra saber si é a 2 refeição
            print(f'{self.nome} já está comendo {alimento}.')
            return # O código para aqui!

        if self.falando:  # Critério pra saber si a pessoa está comendo e que nao pode falar
            print(f'{self.nome} não pode come falando')
            return


        print(f'{self.nome} está comendo {alimento}.') # Critério pra saber si é a 1 refeição
        self.comendo = True

    # Manipulação com á variable comendo! ---------------------------------------
    # Definindo status da função comer, para PARAR de comer
    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return


        print(f'{self.nome} parou de comer.')
        self.comendo = False

    # Manipulação com á variable idade! ---------------------------------------
    # Definindo status da função idade, para o ano
    # Tipo de Métodos
    def get_ano_nascimento(self): # Aqui eu preciso da instancia SELF Método com instancia
        return self.ano_atual - self.idade

    @classmethod # Decorador - Metodo de classe
    def por_ano_nascimento(cls, nome, ano_nascimento): # Aqui eu não preciso da instancia SELF mas é referenta á Class
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)


    @staticmethod # Decorador - Metodo stático
    def gera_id(): # Utilizamos uma instancia ou class, não pode usar cls,self,...
        rand = randint(10000, 19999)
        return rand






