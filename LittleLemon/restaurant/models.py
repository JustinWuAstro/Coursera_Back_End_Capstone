from django.db import models

# Create your models here.

class Booking(models.Model):
    Name = models.CharField(max_length=200)
    No_of_guests = models.SmallIntegerField()
    BookingDate = models.DateField()

    def __str__(self): 
        return f'{self.Name} : {str(self.BookingDate)}'

class Menu(models.Model):
   Title = models.CharField(max_length=200)
   Price = models.DecimalField(max_digits=10, decimal_places=2) 
   Inventory = models.IntegerField(null=False)  

   def __str__(self): 
        return f'{self.Title} : {str(self.Price)}'