class twodigits:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def show(self):
        print(f'Первое число: {self.num1}'
              f' Втооре чилсо: {self.num2}')
    def sum(self):
        return self.num1 + self.num2
    def max(self):
        return max(self.num1, self.num2)
    def change(self,newnum1, newnum2):
        self.num1 = newnum1
        self.num2 = newnum2
insert = twodigits(12, 2)
insert.change(3, 10)
print(insert.show())
print(f'сумма: {insert.sum()}')
print(f'наибольшее: {insert.max()}')