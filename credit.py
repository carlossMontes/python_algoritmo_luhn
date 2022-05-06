#! python3

# Metodo para identificar la marca de la tarjeta
def marca_tarjeta(num):
    mastercard = '51','52','53','54','55'
    american_express = '34','37'
    digitos = len(num)
    if digitos == 16 and num[0] == '4' or digitos == 13:
        return 'Visa'
    elif digitos == 15 and num[:2] in american_express:
        return 'AMEX'
    elif num[:2] in mastercard:
        return 'Mastercard'
    else:
        return 'Desconocida'

# Metodo para validar la tarjeta
def valida(num):
    total = 0
    # Ciclo para la suma de los digitos de la posicion dos al ultimo
    for digitos in num[-2::-2]:
        value = int(digitos) * 2
        total += value if value < 10 else value - 9
    # Suma de todos los demas digitos
    for digitos in num[-1::-2]:
        total += int(digitos)
    if total % 10 == 0:
        return marca_tarjeta(num)
    return 'Invalida'

# Test
print(valida('378282246310005'))
print(valida('6176292929'))
print(valida('4815163025408959'))
print(valida('48151630254089589'))

input()