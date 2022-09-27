from classes import Conta

d1 = Conta('Eliedson', 18812477160, 'eli@gmail.com', 145912578)
d2 = Conta('Ana Julia', 44574175729, 'ana@hotmail.com', 746279512)
d3 = Conta('Iuri', 76103547164, 'iuri@orkut.com', 585296374)

print(vars(d1))
print(vars(d2))
print(vars(d3))

Conta.mudar_cpf(d1, input("Deseja alterar o CPF?"))

Conta.verificar_nome(d2, input("Deseja verificar seu nome?"))

Conta.mostrar_dados(d3)
