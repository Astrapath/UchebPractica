class Calculation:
    def __init__(self):
        self.__calculationLine = None
        self.calculationLine = ''

    def SetCalculationLine(self, line):
        self.__calculationLine = line

    def SetLastSymbolCalculationLine(self, symbol):
        self.__calculationLine += symbol

    def GetCalculationLine(self):
        return self.__calculationLine

    def GetLastSymbol(self):
        return self.__calculationLine[-1]

    def DeleteLastSymbol(self):
        self.__calculationLine = self.__calculationLine[:-1]


calc = Calculation()
calc.SetCalculationLine('9+10')
print(calc.GetCalculationLine())
calc.SetLastSymbolCalculationLine(' = 21')
print(calc.GetCalculationLine())
print(calc.GetLastSymbol())
calc.DeleteLastSymbol()
print(calc.GetCalculationLine())
print(calc.GetLastSymbol())
