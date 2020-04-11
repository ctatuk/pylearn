'''Процентная ставка по вкладу составляет P процентов годовых, которые прибавляются к сумме вклада.
Вклад составляет X рублей Y копеек. Определите размер вклада через год.
Программа получает на вход целые числа P, X, Y и должна вывести два числа: величину вклада через год
в рублях и копейках. Дробная часть копеек отбрасывается.'''

'''p = int(input())
x = int(input())
y = int(input())
vklad = x + y/100+p*x/100+p*y/100/100
vklad1=vklad%1*100
print(int(vklad),end=" ")
print(int(vklad1))'''


def vklad(procent, rubles, kopeek):
    'через год банковский депозит будет такой:'
    bank_deposite = rubles + kopeek / 100 + procent * rubles / 100 + procent * kopeek / 100 / 100

    deposite_kopeek = bank_deposite % 1 * 100
    print(int(bank_deposite), end=" ")
    print(int(deposite_kopeek))
vklad(23, 19382, 23)
