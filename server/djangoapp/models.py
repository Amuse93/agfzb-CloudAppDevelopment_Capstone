from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake (models.Model):
  name = models.CharField(null=False, max_length=30, default='make')
  description = models.CharField(max_length=1000)
  
  def __str__(self):
    return "Name: " + self.name + "," + \
           "Description: " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
  SEDAN = 'sedan'
  COUPE = 'coupe'
  SPORTSCAR = 'sports car'
  STATIONWAGON = 'station wagon'
  HATCHBACK = 'hatchback'
  CONVERTABLE = 'convertable'
  SUV = 'SUV'
  MINIVAN = 'minivan'
  PICKUPTRUCK = 'pickup truck'
  MODEL_TYPES = [
      (SEDAN, 'Sedan'),
      (COUPE, 'Coupe'),
      (SPORTSCAR, 'Sports Car'),
      (STATIONWAGON, 'Station Wagon'),
      (HATCHBACK, 'Hatchback'),
      (CONVERTABLE, 'Convertable'),
      (SUV,'SUV'),
      (MINIVAN,'Minivan'),
      (PICKUPTRUCK, 'Pickup Truck')
  ]
  
  
  carmake = models.ForeignKey(CarMake,on_delete=models.CASCADE)
  dealer_id = models.IntegerField(default=0)
  name = models.CharField(null=False, max_length=30, default='model')
  type = models.CharField(max_length=15, choices=MODEL_TYPES, default=SEDAN)
  year = models.DateField(default=now)
  
def __str__(self):
    return "Name: " + self.name + "," + \
           "Car Make: " + self.carmake + "," + \
           "Dealer_id: " + self.dealer_id + "," \
           "Type: " + self.type + "," + \
           "Year: " + self.year + "."


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
