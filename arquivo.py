# Peça ao usuário para inserir o número de horas extras 
# e o número de horas que o funcionário faltou. Se a 
# quantidade de horas extras for maior que as horas faltadas mais 
# 50%, imprima "Bônus de R$ 500.00". Caso contrário, 
# imprima "Sem bônus".

hora_extra = int(input('Hora-extras'))
hora_ausente = int(input('Horas ausentes:'))

horas_ausentes_50 = (hora_ausente * 1.5)

if hora_extra > horas_ausentes_50:
    print('Bônus de R$ 500,00') 
else:
    print('Sem bônus!')
    
