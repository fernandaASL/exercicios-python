#Um motorista deseja colocar no seu tanque X reais de gasolina. Escreva um algoritmo para ler o
#preço do litro da gasolina e o valor do pagamento, e exibir quantos litros ele conseguiu colocar no
#tanque.

l = float(input('qual o preço do litro da gasolina? '))
p = float(input('qual foi o valor do pagamento? '))
la = p/l
print('Você abasteceu', la, 'litros de gasolina')