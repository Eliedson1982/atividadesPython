class Conta:
    def __init__(self, nome, cpf, email, num, mensagem):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.num = num
        self.mensagem = mensagem

    def verificar_nome(self, resposta):
        if resposta == "y":
            print("nome: {}".format(self.nome))
        else:
            print("Ok!")

    def mudar_cpf(self, resposta):
        if resposta == "y":
            print("Infelizmente isso não é possivel.")
        else:
            print("Ok!")

    def mostrar_dados(self):
        print('Nome:', self.nome, '\nCPF:', self.cpf, '\nEmail:', self.email, '\nNúmero: ', self.num)

    def envia_mensagem(self, destino, msg):
        destino.mensagem = msg
    
