from fractions import Fraction as fr

aa = input("Введите первую дробь в формате a/b")
ab = input("Введите вторую дробь в формате c/d")

if aa.find('/') is True and ab.find('/') is True:
    ba = int(aa.split('/')[-1])
    bb = int(ab.split('/')[-1])
    if (ba and bb) != 0:
        print(fr(aa) + fr(ab))
    else:
        print('Деление на 0')
else:
    print('Error. Не верный формат')
