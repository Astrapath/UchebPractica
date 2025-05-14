class Train:
    def __init__(self, station, number, time):
        self.station = station
        self.number = number
        self.time = time

    def showinfo(self):
        return f'Пункт назначения:{self.station}, номер поезда: {self.number}, время прибытия: {self.time}'


def search(train):
    searchingnumber = input("номер поезда: ")
    if train.number == searchingnumber:
        print(train.showinfo())
    else:
        print('не найдено')
train1 = Train('Москва', '13', '13:30' )
print(train1.showinfo())

search(train1)