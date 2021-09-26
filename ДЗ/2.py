class Road:

    _lenght = 0
    _width = 0

    def asphalt_weight (self):
        weight = (lenght * width * h * 11) / 1000
        print (f'''Для покрытия заданного участка дороги Вам потребуется
{ weight } тонн асфальта''')

win = True

print ('''Данная программа рассчитает требуемую массу асфальта
для покрытия заданного участка дороги.
Для расчётов принимаем плотность асфальта, равную 1,1 г/см3''')
while (win):
    a = Road ()
    lenght = float (input ('Введите требуемую длину участка, км: '))
    lenght = lenght * 1000
    width = float (input ('Введите требуемую ширину полотна, м: '))
    h = float (input ('Введите значение требуемой толщины покрытия, см: '))
    a.asphalt_weight ()
    stop = input ('Рассчитать ещё (Y - да)? ')
    if (stop == 'y'):
        win = True
    else:
        win = False
    
    
