class Curcle:
    def __init__(self,number):
        self.num=number

    def Area(self):
        return 3.14*self.num**self.num
    
    def Peri(self):
        return 2*3.14*self.num
    

getarea=Curcle(4)
print(getarea.Area())
print(getarea.Peri())