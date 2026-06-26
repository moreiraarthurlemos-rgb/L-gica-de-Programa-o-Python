#Mensagem inicial
print('======Validador de Maioridade======')

#Variavel nome usuario
nome = str(input('Digite aqui seu nome :'))
print('Olá {}, no campo abaixo, digite sua idade ok!'.format(nome))

#Variavel - idade usuario
idade = int(input('Insira sua idade :'))

#Lógicas
if idade >=18:
    print("você é maior de idade:")
else:
    print("você é menor de idade")
    
