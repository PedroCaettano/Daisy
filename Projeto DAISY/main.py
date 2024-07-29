import tkinter as tk
from tkinter import messagebox
import re

class Daisy:
    def __init__(self, root):
        self.root = root
        self.root.title("Oi! Eu sou a Daisy, sua Assistente Virtual")
        
        self.perfil_do_usuario = {}
        self.contatos_emergencia = []
        self.frase_ativacao = "Oi Daisy"

        # Interface gráfica
        self.create_widgets()
        
    # Criando uma possível interface gráfica.
    # Inserindo fontes, tamanhos e colocando cada comando em seu lugar pertencido.
    def create_widgets(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)
        
        self.title_label = tk.Label(self.frame, text="Oi! Eu sou a Daisy, sua Assistente Virtual", font=("The Beardy", 18))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        self.ativacao_botao = tk.Button(self.frame, text="Ativar Daisy", command=self.activate)
        self.ativacao_botao.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        self.status_label = tk.Label(self.frame, text="", font=("Frito Vandito", 12))
        self.status_label.grid(row=2, column=0, columnspan=2, pady=(0, 20))
        
        self.menu_botao = tk.Button(self.frame, text="Menu", command=self.menu)
        self.menu_botao.grid(row=3, column=0, columnspan=2, pady=(0, 20))

    def activate(self):
        input_text = "Oi Daisy"
        if re.search(self.frase_ativacao, input_text, re.IGNORECASE):
            self.status_label.config(text="Oi, meu bem! Como posso ajudar?")
            self.menu()
        else:
            self.status_label.config(text="Desculpa, não entendi. Pode por favor repetir?")

    # Criando o perfil do usuário
    # Aqui o usuário insere informações importantes e cruciais que serão responsáveis pelas funcionalidades da Daisy durante
    # o seu tempo de uso. 
    def create_profile(self):
        self.janela_de_perfil = tk.Toplevel(self.root)
        self.janela_de_perfil.title("Vamos criar o seu perfil.")
        
        tk.Label(self.janela_de_perfil, text="Nome Completo:").grid(row=0, column=0)
        self.nome_entry = tk.Entry(self.janela_de_perfil)
        self.nome_entry.grid(row=0, column=1)
        
        tk.Label(self.janela_de_perfil, text="Idade:").grid(row=1, column=0)
        self.idade_entry = tk.Entry(self.janela_de_perfil)
        self.idade_entry.grid(row=1, column=1)
        
        # O idioma será necessário para uma melhor comunicação com o usuário.
        # Neste exemplo estamos trabalhando com o Português como base, mas outras
        # idiomas podem ser usados para uma melhor compreensão do usuário e 
        # dos contatos próximos com o usuário
        tk.Label(self.janela_de_perfil, text="Idioma:").grid(row=2, column=0)
        self.idioma_entry = tk.Entry(self.janela_de_perfil)
        self.idioma_entry.grid(row=2, column=1)

        # A etapa de endereço, bairro, cidade, estado e país são muito importantes!
        # O Motivo disso é para a Daisy se localizar usando o GPS ou qualquer outro meio de geolocalização após
        # o usuário informar tais informações. E também para obter os números oficiais de instituições que possam
        # ajudar ou prestar os primeiros socorros de forma rápida e eficaz
        tk.Label(self.janela_de_perfil, text="Endereço:").grid(row=3, column=0)
        self.endereco_entry = tk.Entry(self.janela_de_perfil)
        self.endereco_entry.grid(row=3, column=1)
        
        tk.Label(self.janela_de_perfil, text="Bairro:").grid(row=4, column=0)
        self.bairro_entry = tk.Entry(self.janela_de_perfil)
        self.bairro_entry.grid(row=4, column=1)
        
        tk.Label(self.janela_de_perfil, text="Cidade:").grid(row=5, column=0)
        self.cidade_entry = tk.Entry(self.janela_de_perfil)
        self.cidade_entry.grid(row=5, column=1)
        
        tk.Label(self.janela_de_perfil, text="Estado:").grid(row=6, column=0)
        self.estado_entry = tk.Entry(self.janela_de_perfil)
        self.estado_entry.grid(row=6, column=1)
        
        tk.Label(self.janela_de_perfil, text="País:").grid(row=7, column=0)
        self.pais_entry = tk.Entry(self.janela_de_perfil)
        self.pais_entry.grid(row=7, column=1)
        
        tk.Button(self.janela_de_perfil, text="Vou salvar essas informações com carinho.", command=self.save_profile).grid(row=8, column=0, columnspan=2)

    # Salvando o perfil
    def save_profile(self):
        self.perfil_do_usuario['Nome Completo'] = self.nome_entry.get()
        self.perfil_do_usuario['Idade'] = self.idade_entry.get()
        self.perfil_do_usuario['Idioma'] = self.idioma_entry.get()
        self.perfil_do_usuario['Endereço'] = self.endereco_entry.get()
        self.perfil_do_usuario['Bairro'] = self.bairro_entry.get()
        self.perfil_do_usuario['Cidade'] = self.cidade_entry.get()
        self.perfil_do_usuario['Estado'] = self.estado_entry.get()
        self.perfil_do_usuario['País'] = self.pais_entry.get()
        
        self.janela_de_perfil.destroy()
        messagebox.showinfo("PRONTO!", "Seu perfil foi criado com sucesso!")
    
    # Adicionando contatos de emergência:
    # A Daisy possui a função de mandar uma mensagem de emergência para contatos próximos do usuário para avisá-los de que ele não está bem.
    # O número máximo de contatos de emergência que podem ser salvos são 5
    def add_contatos_emergencia(self):
        if len(self.contatos_emergencia) < 5:
            self.janela_de_contatos = tk.Toplevel(self.root)
            self.janela_de_contatos.title("Adicione um Contato de Emergência")
            
            tk.Label(self.janela_de_contatos, text="Nome do contato:").grid(row=0, column=0)
            self.nome_contato_entry = tk.Entry(self.janela_de_contatos)
            self.nome_contato_entry.grid(row=0, column=1)
            
            tk.Label(self.janela_de_contatos, text="Número de celular:").grid(row=1, column=0)
            self.numero_contato_entry = tk.Entry(self.janela_de_contatos)
            self.numero_contato_entry.grid(row=1, column=1)
            
            tk.Button(self.janela_de_contatos, text="Salvar", command=self.save_contatos_emergencia).grid(row=2, column=0, columnspan=2)
        else:
            messagebox.showwarning("Contatos de Emergência", "Número máximo de contatos de emergência atingido.")
    
    # Salvando o contato de emergência
    def save_contatos_emergencia(self):
        nome = self.nome_contato_entry.get()
        numero = self.numero_contato_entry.get()
        self.contatos_emergencia.append({'nome': nome, 'numero': numero})
        
        self.janela_de_contatos.destroy()
        messagebox.showinfo("Contato de Emergência", f"Contato {nome} adicionado com sucesso.")

    def display_contatos_emergencia(self):
        informacoes_contato = "\n".join([f"Nome: {contact['nome']}, Telefone: {contact['numero']}" for contact in self.contatos_emergencia])
        messagebox.showinfo("Contatos de Emergência", informacoes_contato)

    # Menu de escolhas:
    # Aqui o usuário pode decidir qual comando usar da Daisy
    def menu(self):
        self.janela_de_menu = tk.Toplevel(self.root)
        self.janela_de_menu.title("Menu")
        
        tk.Button(self.janela_de_menu, text="Criar Perfil", command=self.create_profile).pack(padx=10, pady=5)
        tk.Button(self.janela_de_menu, text="Adicionar Contato de Emergência", command=self.add_contatos_emergencia).pack(padx=10, pady=5)
        tk.Button(self.janela_de_menu, text="Ver Contatos de Emergência", command=self.display_contatos_emergencia).pack(padx=10, pady=5)
        tk.Button(self.janela_de_menu, text="Pesquisar Números de Emergência", command=self.search_emergency_numbers).pack(padx=10, pady=5)
        tk.Button(self.janela_de_menu, text="Realizar Chamada de Emergência", command=self.make_emergency_call).pack(padx=10, pady=5)
        tk.Button(self.janela_de_menu, text="Sair", command=self.janela_de_menu.destroy).pack(padx=10, pady=5)

    def search_emergency_numbers(self):
        pais = self.perfil_do_usuario.get('País', '').lower()
        contatos_emergencia = {
            'brasil': {'bombeiros': '193', 'samu': '192', 'polícia': '190'},
            'estados unidos': {'para todos os serviços de segurança interligados': '911'},
            'inglaterra': {'polícia, ambulância e bombeiros': '999', 'casos não emergenciais': '101', 'procedimentos de saúde não emergenciais': '111'}
            # Adicionar outros países caso necessário
        }

        if pais in contatos_emergencia:
            numbers = contatos_emergencia[pais]
            info = (f"Números de emergência para {self.perfil_do_usuario['País']}:\n"
                    f"Corpo de Bombeiros: {numbers['bombeiros']}\n"
                    f"SAMU: {numbers['samu']}\n"
                    f"Polícia: {numbers['polícia']}")
            messagebox.showinfo("Números de Emergência", info)
        else:
            messagebox.showerror("Erro", "Números de emergência não disponíveis para este país.")

    def make_emergency_call(self):
        if self.perfil_do_usuario.get('País', '').lower() == 'brasil':
            numero_emergencia = '192'  # Exemplo: SAMU no Brasil
        else:
            numero_emergencia = '911'  # Exemplo: Emergência padrão internacional
        messagebox.showinfo("Chamada de Emergência", f"Simulando uma chamada para {numero_emergencia}...")
        
    # Aqui a Daisy realiza o processo de chamada para os contatos de emergência que você inseriu em sua máquina
    def chatbot_response(self, query):
        responses = {
            "oi": "Olá, querido(a)! Como posso ajudar você hoje?",
            "emergência": "Vou te ajudar com a emergência. Vai ficar tudo bem.",
            "atualizar perfil": "Ok. Vamos atualizar seu perfil, querido(a).",
            "contato": "Vou ligar para um contato de emergência. Fique calmo, vai ficar tudo bem.",
        }
        for key in responses:
            if key in query.lower():
                return responses[key]
        return "Pode repetir, por favor?"

    def chatbot(self):
        self.janela_de_chat = tk.Toplevel(self.root)
        self.janela_de_chat.title("Daisy Chatbot")
        
        self.chat_label = tk.Label(self.janela_de_chat, text="Pode perguntar qualquer coisa pra mim, amor")
        self.chat_label.pack(padx=10, pady=5)
        
        self.chat_entry = tk.Entry(self.janela_de_chat, width=50)
        self.chat_entry.pack(padx=10, pady=5)
        
        self.chat_button = tk.Button(self.janela_de_chat, text="Perguntar", command=self.handle_chat)
        self.chat_button.pack(padx=10, pady=5)
        
        self.chat_response_label = tk.Label(self.janela_de_chat, text="", wraplength=400)
        self.chat_response_label.pack(padx=10, pady=5)

    def handle_chat(self):
        query = self.chat_entry.get()
        response = self.chatbot_response(query)
        self.chat_response_label.config(text=response)

if __name__ == "__main__":
    print('''
**************************************************************************************************************************************   
    ,----..                                                                             
   /   /   \                       ,---,                                                
  /   .     :   ,--,             .'  .' `\                ,--,                          
 .   /   ;.  \,--.'|           ,---.'     \             ,--.'|                          
.   ;   /  `i ;|  |,            |   |  .`\  |            |  |,      .--.--.              
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
    root = tk.Tk()
    daisy = Daisy(root)
    root.mainloop()
