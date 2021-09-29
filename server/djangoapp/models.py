from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return 'name= ' + self.name + ', desc= ' + self.des


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    
    TYPE_CHOICES = (
        ('SEDAN', "SEDAN"),
        ('SUV', "SUV"),
        ('WAGON', "WAGON"),
        ('OTHER', "OTHER"),
    )

    model_id = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    dealer_id = models.IntegerField()
    car_type = models.CharField(max_length=10, choices=TYPE_CHOICES) 
    year = models.DateField()

    def __str__(self):
        return 'model_id=' + self.model_id + ', name=' + self.name + \
               ', dealer_id=' + self.dealer_id + ', car_type=' + self.car_type + \
               ', year=' + self.year

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
