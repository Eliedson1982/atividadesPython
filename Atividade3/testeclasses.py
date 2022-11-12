from classes import Conta

contaEliedson = Conta('Eliedson', 13626490085, 'eli@gmail.com', 996714087, '')
contaAna = Conta('Ana Julia', 44574175729, 'ana@hotmail.com', 996456772, '')
contaIuri = Conta('Iuri', 76103547164, 'iuri@orkut.com', 996840281, '')

Conta.mudar_cpf(contaEliedson, input("Deseja alterar o CPF?"))
Conta.verificar_nome(contaAna, input("Deseja verificar seu nome?"))
Conta.mostrar_dados(contaIuri)
contaEliedson.envia_mensagem(contaIuri, input("Olá " + contaEliedson.nome + " escreva sua mensagem para " + contaIuri.nome +":"))
print(contaIuri.mensagem)

print(vars(contaEliedson))
print(vars(contaAna))
print(vars(contaIuri))
