class Worker:

    name = ''
    surname = ''
    position = ''
    wage = 0
    bonus = 0
    _income = dict ( оклад = wage, премия = bonus )


class Position (Worker):

    def get_full_name (self):
        name = input ('Введите имя: ')
        surname = input ('Введите фамилию: ')
        name = (f'Имя:  { name }  { surname}')
        print (name)

    def get_total_income (self):
        position = input ('Должность: ')
        wage = float (input ('Оклад, руб: '))
        bonus = float (input ('Премия, %: '))
        bonus = wage * (bonus / 100)
        income = wage + bonus
        income = (f'Полный доход: { income } руб')
        print (income)
        

a = Position ()
a.get_full_name ()
a.get_total_income ()


