while True:
    try:
        aa = int(input("Данная программа возведет ваше число в 13 степень. Введите число"))
        break
    except ValueError:
        print('Error. Не верный формат')
print('Результат возведения в степень числа', aa, aa**13)
