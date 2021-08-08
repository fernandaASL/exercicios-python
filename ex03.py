# Escreva um algoritmo para ler o nome e a idade de uma pessoa, e exibir quantos dias de vida
#ela  possui.  Considere  sempre  anos  completos,  e  que  um  ano  possui  365  dias.  Ex:  uma  pessoa
#com 19 anos possui 6935 dias de vida; veja um exemplo de saída: MARIA, VOCÊ JÁ VIVEU 6935
#DIAS

n = str(input('escreva o seu nome: '))
i = int(input('escreva sua idade: '))
dv = i * 365
print('Olá, {}, você tem {} dias de vida'.format(n, dv))