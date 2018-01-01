import json

class Pessoa:
    dados = {}
    
    def add_atribute(self):
        """Adiçao de keys e valores para uma pessoa"""
        key = input('Digite o nome do novo atributo:').strip(' ').capitalize()
        value = input('{}:'.format(key))
        
        dado = { key:value }
        self.dados.update(dado)

class DataBank():
    pessoas = []
    
    def add_pessoas(self, pessoa):
        """Adicionar objeto pessoa a lista de pessoas"""
        self.pessoas.append(pessoa.dados)

    def salvar_json(self):

        def jdefault(o): #configura o json para receber objetos
            return o.__dict__
        with open('data_bank.json', 'w') as data_bankjson:
            json.dump(self.pessoas, data_bankjson)

    def carregar_bank(self):
        try:
            with open('data_bank.json', 'r') as databankjson:
                self.pessoas = json.load(databankjson)
        except FileNotFoundError:
            print('Arquivo JSON não encontrado!')

pessoas = DataBank()
while(True):
        print('---MENU---')
        print('1. Adicionar uma nova pessoa.')
        print('2. Salvar dados.')
        print('3. Carregar dados')
        
        option = input('Escolha:')
        
        if option == '1':
            while True:     
                pessoa = Pessoa()
                pessoa.add_atribute()
                
                continua = input('Continuar adicionando atributos? "Y" ou "N"').capitalize()
                
                if continua == 'N':
                    pessoas.add_pessoas(pessoa)
                    break
                    
        elif option == '2':
            pessoas.salvar_json()
            
        elif option == '3':
            pessoas.carregar_bank()
