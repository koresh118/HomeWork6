from random import randrange

class Car:

    speed = 0
    color = ''
    name = ''
    is_police = False

    def car_go (self):
        print ('Машина поехала')

    def car_stop (self):
        print ('Машина остановилась')

    def car_turn (self):
        x = randrange (0, 1, 1)
        if (x == 0):
            print ('Машина повернула налево')
        else:
            print ('Машина повернула направо')

    def show_speed (self):
        speed = randrange (0, 160, 1)
        print (f'Текущая скорость машины - { speed } км/ч')
        

class TownCar (Car):
    name = 'Lincoln Town Car'
    color = 'цвет чёрный'
    is_police = False

    def show_speed (self):
        speed = randrange (0, 160, 1)
        print (f'Текущая скорость машины - { speed } км/ч')
        if (speed > 60):
            print ('Автомобиль превышает установленную максимальную скорость!')
    

class SportCar (Car):
    name = 'Toyota Supra'
    color = 'цвет красный'
    is_police = False


class WorkCar (Car):
    name = 'Mack 600'
    color = 'цвет серый'
    is_police = False

    def show_speed (self):
        speed = randrange (0, 160, 1)
        print (f'Текущая скорость машины - { speed } км/ч')
        if (speed > 40):
            print ('Автомобиль превышает установленную максимальную скорость!')


class PoliceCar (Car):
    name = 'Police Car'
    color = 'цвет специальный'
    is_police = True


win = True

while (win):
    a = int (input ('Выберите модель авто, выбрав цифру от 1 до 4: '))
    if (a == 1):
        a = TownCar ()
    elif (a == 2):
        a = SportCar ()
    elif (a == 3):
        a = WorkCar ()
    elif (a == 4):
        a = PoliceCar ()
    print (a.name)
    print (a.color)
    print (a.is_police)
    y = randrange (1, 3, 1)
    if (y == 1):
        a.car_go ()
        a.show_speed ()
    elif (y == 2):
        a.car_stop ()
    elif (y == 3):
        a.car_turn ()
    z = input ('Хотите выбрать ещё машину (Y - да)? ')
    if (z == 'y'):
        win = True
    else:
        win = False
    
