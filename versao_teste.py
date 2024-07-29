# Rascunho do código:
import re

class Daisy:
    def __init__(self):
        self.user_profile = {}
        self.emergency_contacts = []
        self.activation_phrase = "Oi Daisy"

    def activate(self, input_text):
        if re.search(self.activation_phrase, input_text, re.IGNORECASE):
            print("Daisy ativada. Como posso ajudar?")
            self.menu()
        else:
            print("Comando não reconhecido. Diga 'Oi Daisy' para ativar.")

    def create_profile(self):
        print("Vamos criar seu perfil.")
        self.user_profile['nome'] = input("Nome: ")
        self.user_profile['idade'] = input("Idade: ")
        self.user_profile['idioma'] = input("Idioma: ")
        self.user_profile['endereço'] = input("Endereço: ")
        self.user_profile['bairro'] = input("Bairro: ")
        self.user_profile['cidade'] = input("Cidade: ")
        self.user_profile['estado'] = input("Estado: ")
        self.user_profile['país'] = input("País: ")
        print("Perfil criado com sucesso!")

    def add_emergency_contact(self):
        if len(self.emergency_contacts) < 5:
            name = input("Nome do contato: ")
            phone = input("Número de celular: ")
            self.emergency_contacts.append({'name': name, 'phone': phone})
            print(f"Contato {name} adicionado com sucesso.")
        else:
            print("Número máximo de contatos de emergência atingido.")

    def display_emergency_contacts(self):
        print("Contatos de emergência:")
        for contact in self.emergency_contacts:
            print(f"Nome: {contact['name']}, Telefone: {contact['phone']}")

    def menu(self):
        print('''
        Escolha uma opção:
        1. Criar perfil
        2. Adicionar contato de emergência
        3. Ver contatos de emergência
        4. Pesquisar números de emergência
        5. Realizar chamada de emergência
        6. Sair
        ''')
        option = input("Opção: ")
        if option == '1':
            self.create_profile()
        elif option == '2':
            self.add_emergency_contact()
        elif option == '3':
            self.display_emergency_contacts()
        elif option == '4':
            self.search_emergency_numbers()
        elif option == '5':
            self.make_emergency_call()
        elif option == '6':
            print("Saindo...")
        else:
            print("Opção inválida. Tente novamente.")
            self.menu()

    def search_emergency_numbers(self):
        # Função para pesquisar números de emergência com base na localização do usuário
        country = self.user_profile.get('país', '').lower()
        emergency_numbers = {
            'brasil': {'bombeiros': '193', 'samu': '192', 'polícia': '190'},
            # Adicionar outros países conforme necessário
        }
        if country in emergency_numbers:
            numbers = emergency_numbers[country]
            print(f"Números de emergência para {self.user_profile['país']}:")
            print(f"Corpo de Bombeiros: {numbers['bombeiros']}")
            print(f"SAMU: {numbers['samu']}")
            print(f"Polícia: {numbers['polícia']}")
        else:
            print("Números de emergência não disponíveis para este país.")

    def make_emergency_call(self):
        print("Simulando uma chamada de emergência...")

if __name__ == "__main__":
    daisy = Daisy()
    print('''
**************************************************************************************************************************************   
    ,----..                                                                             
   /   /   \                       ,---,                                                
  /   .     :   ,--,             .'  .' `\                ,--,                          
 .   /   ;.  \,--.'|           ,---.'     \             ,--.'|                          
.   ;   /  ` ;|  |,            |   |  .`\  |            |  |,      .--.--.              
;   |  ; \ ; |`--'_            :   : |  '  |  ,--.--.   `--'_     /  /    '       .--,  
|   :  | ; | ',' ,'|           |   ' '  ;  : /       \  ,' ,'|   |  :  /`./     /_ ./|  
.   |  ' ' ' :'  | |           '   | ;  .  |.--.  .-. | '  | |   |  :  ;_    , ' , ' :  
'   ;  \; /  ||  | :           |   | :  |  ' \__\/: . . |  | :    \  \    `./___/ \: |  
 \   \  ',  / '  : |__         '   : | /  ;  ," .--.; | '  : |__   `----.   \.  \  ' |  
  ;   :    /  |  | '.'|        |   | '` ,/  /  /  ,.  | |  | '.'| /  /`--'  / \  ;   :  
   \   \ .'   ;  :    ;        ;   :  .'   ;  :   .'   \;  :    ;'--'.     /   \  \  ;  
    `---`     |  ,   /         |   ,.'     |  ,     .-./|  ,   /   `--'---'     :  \  \ 
               ---`-'          '---'        `--`---'     ---`-'                  \  ' ; 
                                                                                  `--`        

**************************************************************************************************************************************        
      ''')

    while True:
        user_input = input("Você: ")
        daisy.activate(user_input)
