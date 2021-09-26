import time

class Traffic_Light:

    __color = ''

    def traffic_light_running (color):
        color = 'Всем стоять! Горит КРАСНЫЙ'
        print (color)
        time.sleep (7)
        color = 'ЖЁЛТЫЙ. Приготовиться...'
        print (color)
        time.sleep (2)
        color = 'ЗЕЛЁНЫЙ. Поехали!'
        print (color)
        time.sleep (10)

win = True

while (win):
    a = Traffic_Light ()
    a.traffic_light_running ()
    print (' ' * 75)
    print ('*' * 75)
    b = input ('Запустить ещё раз (Y-да)? ')
    if (b == 'y'):
        win = True
    else:
        win = False
