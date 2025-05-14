class Student:
    def __init__(self, lastname, birthdate, group, grade):
        self.lastname = lastname
        self.birthdate = birthdate
        self.group = group
        self.grade = grade

    def changelastname(self, newlastname):
        self.lastname = newlastname

    def changebirthdate(self, newbirthdate):
        self.birthdate = newbirthdate

    def changegroup(self, newgroup):
        self.group = newgroup

    def showinfo(self):
        return (f'Фамилия:{self.lastname}, дата рождения: {self.birthdate},Группа: {self.group}'
                f'успеваемость: {self.grade}')


def searching(student):
    searchlastname = input('фамилия студента: ')
    searchbirthdate = input('дата рождения студента (DD.MM.YYYY): ')
    if student.lastname == searchlastname and student.birthdate == searchbirthdate:
        print(student.showinfo())
    else:
        print("не найден")



student1 = Student("Раковицэ", '05.02.2007', '634', [4, 5, 5, 5, 4])
student1.changelastname("Пхалагов")
student1.changebirthdate('25.05.2007')
student1.changegroup('636')
print(student1.showinfo())

searching(student1)