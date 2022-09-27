class Conta:
    def __init__(self, nome, cpf, email, num):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.num = num

    def verificar_nome(self, resposta):
        if resposta == "y":
            print("nome: ", self.nome)
            return True
        else:
            print("Ok!")
            return False

    def mudar_cpf(self, resposta):
        if resposta == "y":
            print("Infelizmente isso não é possivel.")
        else:
            print("Ok!")

    def mostrar_dados(self):
        print('\nNome: ', self.nome,'\nCPF: ', self.cpf, '\nEmail: ', self.email, '\nNúmero: ', self.num)
