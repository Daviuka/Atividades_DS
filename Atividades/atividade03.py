# FIXME:Sistema de dois valores variáveis do usuário
print("\n")
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

print('-----------------')
print(f'O resultado da soma foi: {soma}')
print(f'O resultado da subtração foi: {sub}')
print(f'O resultado da multiplicação foi: {mult}')
print(f'O resultado da divisão foi: {divi:.2f}')
print('-----------------')
print("\n")
'''
   Crie um sistema onde o usuário irá inserir dois valores, guarde cada valor em variáveis, 
    em seguida vocês irão realizar as 4 operações básicas de matemática (+; -; *, /) e mostrar esses 
    resultados na tela, também concatenados a um texto indicativo de cada operação.
'''