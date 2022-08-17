class Car:
    def __init__(self,make,model,year):
        #initialising attributes
        self.make=make
        self.model=model
        self.year=year
    def descriptive(self):
        long_name=str(self.year)+" "+self.make+ " "+self.model
        return long_name.title()
    
newCar=Car('Audi','A4',2020)
print(newCar.descriptive())
    