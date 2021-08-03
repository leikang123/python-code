"""写一个父亲类"""
class Car():

    def __init__(self,name,model,year):
        self.name = name
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_dec_name(self):
        long_name = str(self.year) + ' ' + self.name+' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print(" this has is "+str(self.odometer_reading) + "noe is ")

    def updatre_odoemeter(self,mileage):
        if mileage >=self.odometer_reading:
            self.odometer_reading = mileage
        else :
            print("you call")
    def increment_odoeter(self,miles):
        self.odometer_reading +=miles

class electirc(Car) :

    def __init__(self,name,model,year):
        super().__init__(name,model,year)
        self.b_size = 70

    def desc_b_size(self):
        print(" This is has a " +str(self.b_size)+ " -ben.")

my_test = electirc('tsa','model',2022)
print(my_test.get_dec_name())
my_test.desc_b_size()
