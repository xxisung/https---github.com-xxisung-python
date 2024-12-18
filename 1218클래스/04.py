class Calculator:
    def setdata(self,first,second):
        self.first = first
        self.second = second
    def sum(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
cal1 = Calculator()
cal1.setdata(4,2)
print("%d와 %d 계산"%(cal1.first,cal1.second))
print("덧셈:",cal1.sum())
print("곱셈:",cal1.mul())
print("뺼셈:",cal1.sub())
print("나눗셈:",cal1.div(),"\n")

cal2 = Calculator()
cal2.setdata(3,5)
print("%d와 %d 계산"%(cal1.first,cal1.second))
print("덧셈:",cal2.sum())
print("곱셈:",cal2.mul())
print("뺼셈:",cal2.sub())
print("나눗셈:",cal2.div(),"\n")