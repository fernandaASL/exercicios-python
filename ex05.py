#Três amigos, Carlos, André e Felipe. decidiram rachar igualmente a conta de um bar. Faça um
#algoritmo para ler o valor total da conta e imprimir quanto cada um deve pagar, mas faça com que
#Carlos  e  André  não  paguem  centavos.

conta = float(input('qual o valor da conta? '))
div = int(conta/3)
carlos = div
andre = div
rest = conta % 3
print('///////: ', rest)
felipe = float(div + rest)
print('Carlos vai pagar:', carlos, 'andre irá pagar:', andre, 'e felipe irá pagar:', felipe)