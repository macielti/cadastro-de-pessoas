
import json
import codecs

class Pessoa:
    dados = {'Nome':''}
    
    def __init__(self):
        nome = input('Digite o nome da pessoa:')
        self.dados['Nome'] = nome.title().strip(' ')
        
    def add_atribute(self):
        while True:
   
            key = input('Digite o nome do novo atributo:').strip(' ').capitalize()
            value = input('{}:'.format(key))
            dado = { key:value }
            self.dados.update(dado)
            
            continua = input('Continuar adicionando atributos? "Y" ou "N"').capitalize()
                
            if continua == 'N':
                break

class DataBank():
    pessoas = [] #lista de pessoas
    
    def add_pessoas(self, pessoa):
        """Adicionar objeto pessoa a lista de pessoas"""
        self.pessoas.append(pessoa.dados)

    def salvar_json(self):
        """Exportar a lista de pessoas para um json"""
        def jdefault(o): #configura o json para receber objetos
            return o.__dict__
        with open('data_bank.json', 'w', encoding="utf-8") as data_bankjson:
            json.dump(self.pessoas, data_bankjson)

    def carregar_bank(self):
        """Carrega os dados do json da lista de pessoas"""
        try:
            with open('data_bank.json', 'r') as databankjson:
                self.pessoas = json.load(databankjson)
        except FileNotFoundError:
            print('')
            
    def listar_pessoas(self):
        """Listar os dados das pessoas salvas"""
        position = 0 
        for pessoa in self.pessoas:
            print('----\nPosição: {}\nNome: {}\n----'.format(pessoa['Nome'], position))
            position += 1
            
    def remov_pessoa(self):
        self.listar_pessoas()
        number = int(input('Digite o numero da posição:'))
        del(self.pessoas[number])
        
        

                

pessoas = DataBank()

pessoas.carregar_bank()

while(True):
        print('---MENU---')
        print('1. Adicionar uma nova pessoa.')
        print('2. Listar todas as pessoas.')
        print('3. Excluir uma pessoa.')
        print('0. Salvar e sair.')
        
        option = input('Escolha:')
        
        if option == '1':
            pessoa = Pessoa()
            pessoa.add_atribute()
            pessoas.add_pessoas(pessoa)
 
                
        
        elif option == '2':
            pessoas.listar_pessoas()
        
        elif option == '3':
            pessoas.remov_pessoa()
                    
        elif option == '0':
            pessoas.salvar_json()
            break
            
