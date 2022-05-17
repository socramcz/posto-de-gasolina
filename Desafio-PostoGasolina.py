print('-=' * 25)
print('BEM VINDO AO POSTO 4BALA')
print('-=' * 25)

litro = float(input('Quantos litros quer abastecer? '))
tipo = str(
    input('Qual o tipo da gasolina? Sendo A (alcool), G (Gasolina)\n')).lower()

alcool = 5.30
gasolina = 7.90

if tipo == 'a':
    total = alcool * litro

    if litro <= 20:
        desconto = litro * (3/100)
        print(
            f'Voce teve um desconto de 3% (R${desconto:.2f}), O total é R${total-desconto:.2f}')

    else:
        desconto2 = litro * (5/100)
        print(
            f'Voce teve um desconto de 5% ({desconto2:.2f}), o total ficou R${total-desconto2:.2f}')

elif tipo == 'g':
    total2 = gasolina * litro

    if litro <= 20:
        desconto3 = litro * (4/100)
        print(
            f'Voce teve um desconto de 4% (R${desconto3:.2f}), o total ficou R${total2-desconto3:.2f}')

    else:
        desconto4 = litro * (6/100)
        print(
            f'Voce teve um desconto de 4% (R${desconto4:.2f}), o total ficou R${total2-desconto4:.2f}')

else:
    print('Codigo invalido')