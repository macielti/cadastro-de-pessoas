
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
    
    def att_dado(self):
        self.listar_pessoas()
        posicao = int(input('Digite a posição da pessoa a ser atualizada:'))
        print('---Chaves---')
        for i in range(len(self.pessoas)):
            for key, value in self.pessoas[i].items():
                print('{}: {}'.format(key, value))
        chave = input('Digite o nome da chave a ser alterada:').capitalize()
        
        try:
            self.pessoas[posicao][chave] = input('Digite o novo valor: ')
        except:
            print('Key not found.')
            
    def exp_html(self):
        with open('pessoas.html', 'w') as people:
            people.writelines('<meta charset="UTF-8">\n')
            people.writelines('<h1>Pessoas</h1>\n')
            for i in range(len(self.pessoas)):
                people.writelines('<hr>\n')
                people.writelines('<h3>Nome:{}</h3><br>\n'.format(self.pessoas[i]['Nome']))
                for key, value in self.pessoas[i].items():
                    people.writelines('<p><b>{}</b>: {}</p>\n'.format(key, value))    
        
        
        
 

pessoas = DataBank()

pessoas.carregar_bank()

while(True):
        print('---MENU---')
        print('1. Adicionar uma nova pessoa.')
        print('2. Listar todas as pessoas.')
       
        print('3. Excluir uma pessoa.')
        print('4. Atualizar um atributo de uma pessoa já cadatrada ou adicionar um novo.')
        print('5. Exportar pessoas para HTML')
        print('0. Salvar e sair.')
        
        option = input('Escolha:')
        
        if option == '1':
            pessoa = Pessoa()
            pessoa.add_atribute()
            pessoas.add_pessoas(pessoa)
            pessoas.salvar_json()
 
                
        
        elif option == '2':
            pessoas.listar_pessoas()
            
            
        elif option == '3':
            pessoas.remov_pessoa()
            pessoas.salvar_json()
            
        elif option == '4':
            pessoas.att_dado()
            pessoas.salvar_json()
        
        elif option == '5':
            pessoas.exp_html()

                    
        elif option == '0':
            pessoas.salvar_json()
            break
            
