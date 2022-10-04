from classes import Conta, Banco

contaEliedson = Conta('Eliedson', 13626490085, 'eli@gmail.com', 996714087, '')
contaAna = Conta('Ana Julia', 44574175729, 'ana@hotmail.com', 996456772, '')
contaIuri = Conta('Iuri', 76103547164, 'iuri@orkut.com', 996840281, '')

b1 = Banco('123-4', contaEliedson, 150, 1000)
b2 = Banco('910-0', contaAna, 170, 1700)
b3 = Banco('567-8', contaIuri, 200, 2000)


Conta.mudar_cpf(contaEliedson, input("Deseja alterar o CPF?"))

Conta.verificar_nome(contaAna, input("Deseja verificar seu nome?"))

Conta.mostrar_dados(contaIuri)

contaEliedson.envia_mensagem(contaIuri, input("Olá " + contaEliedson.nome + " escreva sua mensagem para " + contaIuri.nome +":"))
print(contaIuri.mensagem)

print(b1.titular.nome)
print(b2.titular.num)
print(b3.titular.email)

b2.saca(2600)
b2.extrato()

b1.deposita(50)
b1.extrato()

print(vars(contaEliedson))
print(vars(contaAna))
print(vars(contaIuri))
