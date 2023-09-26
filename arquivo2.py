# Escreva um programa que dê descontos de acordo com o valor da compra:
# acima de R$100, desconto de 10%; entre R$50 e R$100, desconto de 5%;
# abaixo de R$50, sem desconto. Calcule e mostre o valor do desconto 
# e o valor total a pagar.

valor_da_compra= float(input('Digite o valor da nota:'))


if valor_da_compra > 100:
    valor_da_compra -= (valor_da_compra * 1.0)

elif 50 <= valor_da_compra <= 100:
    valor_da_compra -= (valor_da_compra * 0.05)

elif valor_da_compra< 50:
    valor_da_compra = valor_da_compra

print(f'O valor total a pagar é de R$ {valor_da_compra}')
