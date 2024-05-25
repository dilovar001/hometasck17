class Vehicle:
    def __init__(self,max_speed,mileage):
        self.speed=max_speed
        self.mile=mileage

toyota=Vehicle(280,10)
print(toyota.speed," ",toyota.mile)