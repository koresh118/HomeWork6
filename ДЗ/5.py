class Stationery:

    title = ''

    def draw (self):
        print ('Запуск отрисовки')


class Pen (Stationery):
    title = 'Ручка'

    def draw (self):
        print ('Чертит тонкой и чёткой линией.')
    
class Pencil (Stationery):
    title = 'Карандаш'

    def draw (self):
        print ('Чертит тонкой линией. След легко удаляется ластиком.')
    
    
class Handle (Stationery):
    title = 'Маркер'

    def draw (self):
        print ('Чертит широкой линией. Очень хорошо заметен.')


win = True

while (win):
    a = int (input ('Введите номер изделия (1, 2 или 3): '))
    if (a == 1):
        a = Pen ()
    if (a == 2):
        a = Pencil ()
    if (a == 3):
        a = Handle ()
    print (a.title)
    a.draw ()
    x = input ('Хотите попробовать ещё (Y - да)? ')
    if (x == 'y'):
        win = True
    else:
        win = False
