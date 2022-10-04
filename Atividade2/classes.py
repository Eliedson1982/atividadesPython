class Banco:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def deposita(self, valor):
        self.saldo += valor 

    def saca(self, valor):
        if (self.saldo < valor):
            print("Não foi possível realizar o saque.")
        else:
            self.saldo -= valor

    def extrato(self):
        print("Titular: {}  \n  Saldo: {}" .format(self.titular, self.saldo))

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
        print("Seus dados são:")
        print('Nome:', self.nome, '\nCPF:', self.cpf, '\nEmail:', self.email, '\nNúmero: ', self.num)

    def envia_mensagem(self, destino, msg):
        destino.mensagem = msg
