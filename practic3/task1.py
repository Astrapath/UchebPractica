class Worker:
    def __init__(self, name, surname, rate, days):
        self.name = name
        self.surname = surname
        self.rate = rate
        self.days = days

    def getsalary(self):
        salary = self.rate * self.days
        return salary


worker1 = Worker("Олег", "Раковицэ", 1000, 15)
print(f'{worker1.name} {worker1.surname}, ставка: {worker1.rate}, дней работы: {worker1.days}, '
      f'зарплата: {worker1.getsalary()}')
