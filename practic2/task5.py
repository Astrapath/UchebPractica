class new:
    def __init__(self, obj1 = 0, obj2= 0):
        self.obj1 = obj1
        self.obj2 = obj2
    def __del__(self):
        print("объект new с obj1 и obj2 удален")
class default:
    def __init__(self):
        self.obj1 = 1
        self.obj2 = 1
    def __del__(self):
        print('объект default с obj1 и obj2 удален')
objectsnew = new(11, 2)
print(f'new: obj1 = {objectsnew.obj1}, obj2 = {objectsnew.obj2}')
objectsdefault = default()
print(f'default: obj1 = {objectsdefault.obj1}, obj2 = {objectsdefault.obj2}')
del objectsdefault
del objectsnew