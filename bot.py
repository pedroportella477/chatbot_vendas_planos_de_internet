import smtplib
import requests

class Eliz:
    def __init__(self):
        print("Olá! Sou Eliz, estou aqui para oferecer a melhor experiência em planos de acesso à internet em ultra velocidade.")
    
    def iniciar_venda(self):
        resposta = input("Gostaria de fazer o cadastro e receber uma oferta? (Digite 1 para sim, 2 para não): ")
        if resposta == '2':
            print("Agradecemos o contato! Até logo.")
            return
        
        nome = input("Por favor, informe seu nome completo: ")
        data_nascimento = input("Informe sua data de nascimento (DD/MM/AAAA): ")
        cpf_cnpj = input("Informe seu CPF ou CNPJ: ")
        
        cep = input("Informe seu CEP: ")
        endereco = self.consultar_endereco(cep)
        print("Endereço encontrado:", endereco)
        confirmacao_endereco = input("O endereço está correto? (Digite 1 para sim, 2 para não): ")
        if confirmacao_endereco == '2':
            endereco = input("Por favor, informe seu endereço completo: ")
        
        numero_residencia = input("Informe o número da residência: ")
        complemento = input("Informe o complemento (se houver): ")
        ponto_referencia = input("Informe um ponto de referência: ")
        
        telefone = input("Informe seu telefone para contato: ")
        whatsapp = input("Você possui WhatsApp? (Digite sim ou não): ")
        
        email = input("Informe seu e-mail: ")
        
        self.mostrar_planos()
        plano = input("Selecione o plano desejado (Digite o número correspondente): ")
        
        vencimento = input("Informe a data de vencimento desejada (5, 10, 15, 25): ")
        
        print("\nResumo da Contratação:")
        print(f"Nome: {nome}")
        print(f"Data de Nascimento: {data_nascimento}")
        print(f"CPF/CNPJ: {cpf_cnpj}")
        print(f"Endereço: {endereco}, {numero_residencia} - {complemento}, {ponto_referencia}")
        print(f"Telefone: {telefone}")
        print(f"WhatsApp: {whatsapp}")
        print(f"E-mail: {email}")
        print(f"Plano escolhido: {plano} - {self.obter_nome_plano(plano)}")
        print(f"Data de vencimento: {vencimento}")
        
        confirmacao_contratacao = input("Deseja confirmar a contratação? (Digite 1 para sim, 2 para cancelar): ")
        if confirmacao_contratacao == '2':
            print("Que pena! Lamentamos o cancelamento do seu pedido.")
            return
        
        # Envio de e-mails
        self.enviar_email_cliente(nome, email)
        self.enviar_email_empresa(nome, email)
        
        print("Obrigado pela preferência! Você receberá um contato em breve para agendar sua instalação.")
        
    def consultar_endereco(self, cep):
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        data = response.json()
        endereco = f"{data['logradouro']}, {data['bairro']}, {data['localidade']} - {data['uf']}"
        return endereco
    
    def obter_nome_plano(self, plano):
        planos = {
            '1': '50MB',
            '2': '100MB',
            '3': '150MB',
            '4': '200MB',
            '5': '300MB',
            '6': '500MB'
        }
        return planos.get(plano, 'Plano Inválido')
        
    def mostrar_planos(self):
        print("\nPlanos de Acesso à Internet via Fibra Óptica:")
        print("1. 50MB")
        print("2. 100MB")
        print("3. 150MB")
        print("4. 200MB")
        print("5. 300MB")
        print("6. 500MB")
    
    def enviar_email_cliente(self, nome, email):
        subject = "Pedido de Instalação Realizado com Sucesso"
        body = f"Olá {nome},\n\nSeu pedido de instalação foi realizado com sucesso!\n\nAtenciosamente,\nEquipe Delta Telecom"
        self.enviar_email(email, subject, body)
    
    def enviar_email_empresa(self, nome, email):
        subject = "Nova Possível Venda"
        body = f"Uma nova possível venda foi realizada por {nome}.\n\nDetalhes do cliente:\nNome: {nome}\nE-mail: {email}"
        self.enviar_email("suportedeltatelecom@gmail.com", subject, body)
    
    def enviar_email(self, to_email, subject, body):
        gmail_user = "suportedeltatelecom@gmail.com"
        gmail_password = "@Delta477"
        
        email_text = f"From: {gmail_user}\nTo: {to_email}\nSubject: {subject}\n\n{body}"
        
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(gmail_user, gmail_password)
            server.sendmail(gmail_user, to_email, email_text)
            server.close()
            print("E-mail enviado com sucesso!")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

# Exemplo de uso
eliz = Eliz()
eliz.iniciar_venda()
