from django.db import models

# Create your models here.

std_choice = (
    ('V','V'),('VI','VI'),('VII','VII'),('VIII','VIII'),('IX','IX'),('X','X')
)

div_choice = (
    ('A','A'),('B','B'),('C','C')
)

class Students(models.Model):
    name = models.CharField(max_length=22)
    phone = models.IntegerField()
    seat_no = models.IntegerField()
    std = models.CharField(max_length=4 , choices=std_choice , default='5')
    div = models.CharField(max_length=1 , choices=div_choice , default='A')

