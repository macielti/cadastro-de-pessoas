
import json
import codecs

class Pessoa:
    dados = {}
    
    def add_atribute(self):
        """Adiçao de keys e valores para o dicionário da pessoa"""
        key = input('Digite o nome do novo atributo:').strip(' ').capitalize()
        value = input('{}:'.format(key))
        dado = { key:value }
        self.dados.update(dado)

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
        for pessoa in self.pessoas:
            for key, value in pessoa.items():
                print(key+':'+value)
        

pessoas = DataBank()

pessoas.carregar_bank()

while(True):
        print('---MENU---')
        print('1. Adicionar uma nova pessoa.')
        print('2. Listar todas as pessoas.')
        print('0. Salvar e sair.')
        
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
            pessoas.listar_pessoas()
                    
        elif option == '0':
            pessoas.salvar_json()
            break
            
