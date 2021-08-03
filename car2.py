
class Car2():

      def __init__(self, make, model, year):
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 45

      @property
      def get_des_name(self):
            long_name = str(self.year) + ' ' + self.make + ' ' + self.model
            """ 格式与上层对齐，不然报错"""
            return long_name.title()

      def read_odometer(self):
            print("This is car " + str(self.odometer_reading) + " mils on it")

      def update_odometer(self, mileage):
            self.odometer_reading = mileage

      def increment_odometer(self,miles):
            self.odometer_reading += miles


my_new_car = Car2('audi', 'bb', 876)
print(my_new_car.get_des_name)
my_new_car.update_odometer(49)
my_new_car.read_odometer()
my_new_car.increment_odometer(1000)
my_new_car.read_odometer()
