class Counter:
    def __init__(self, startvalue=0):
        self.value = startvalue

    def plus(self):
        self.value += 1

    def minus(self):
        self.value -= 1


default = Counter()
print(f'по умолчанию: {default.value}')
default.plus()
print(f'увеличение: {default.value}')
default.minus()
print(f'уменьшение:  {default.value}')
custom = Counter(25)
print(f'произвольное: {custom.value}')
custom.plus()
print(f'увеличение: {custom.value}')
custom.minus()
print(f'уменьшение:  {custom.value}')