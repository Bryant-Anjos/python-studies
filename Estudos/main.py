nome = input('Qual o seu nome? ')
idade = int(input('Qual a sua idade? '))
print(type(idade))

print('Seja bem vindo {} de {} anos'.format(nome, idade))
print('{}, daqui a 5 anos você terá {} anos'.format(nome, idade + 5))
