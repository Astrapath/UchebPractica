class Worker:
    def __init__(self, name, surname, rate, days):
        self.__name = name
        self.__surname = surname
        self.__rate = rate
        self.__days = days

    def getsalary(self):
        salary = self.__rate * self.__days
        return salary

    def getname(self):
        return self.__name

    def getsurname(self):
        return self.__surname

    def getrate(self):
        return self.__rate

    def getdays(self):
        return self.__days


worker1 = Worker("Олег", "Раковицэ", 1000, 15)
print(f'{worker1.getname()} {worker1.getsurname()}, ставка: {worker1.getrate()}, дней работы: {worker1.getdays()}, '
      f'зарплата: {worker1.getsalary()}')
