# FIXME:Sistema de dois valores variáveis do usuário
print("\n")
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))

print('-----------------')
num1 = input('Digite o primeiro numero: ')
num1 = int(num1)
print('-----------------')
num2 =  int(input('Digite o segundo numero: '))
print('-----------------')

# FIXME:Operadoes matemático
soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
divi = num1 / num2

print("\n")
print('-----------------')
print(f"O nome é {nome}")
print(f'A sua idade é: {idade}')
print('-----------------')
print(f'O resultado da soma foi: {soma}')
print(f'O resultado da subtração foi: {sub}')
print(f'O resultado da multiplicação foi: {mult}')
print(f'O resultado da divisão foi: {divi:.2f}')
print('-----------------')
print("\n")



'''
    Declare 2 variáveis, cada uma com um valor, e some os resultados concatenados a um texto.
    
    Crie um sistema onde o usuário irá inserir dois valores, guarde cada valor em variáveis, 
em seguida vocês irão realizar as 4 operações básicas de matemática (+; -; *, /) e mostrar esses 
resultados na tela, também concatenados a um texto indicativo de cada operação.
    
    Crie um sistema que receba o nome do usuário, a idade só podendo aceitar numero inteiro, 
em seguida mostre o nome e idade do usuário e peça que ele digite 2 números para que sejam somados. 
Mostrar por último a soma realizada para o usuário.

'''