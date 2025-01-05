from django.db import models
from django.core.exceptions import ValidationError
import re


def validate_only_letters(value):
    if not re.match('^[A-Za-z ]*$', value):  # Regex to match only letters and spaces
        raise ValidationError('Only letters and spaces are allowed.')


def validate_mobile_number(value):
    pattern = r'^\+?[1-9]\d{1,14}$'
    if not re.match(pattern, value) or len(value) < 10:
        raise ValidationError('Invalid mobile number format. Must be at least 10 digits long.')
    if len(value) > 15:
        raise ValidationError('Mobile number cannot be more than 15 digits long.')


def validate_expenses(value):
    if not re.match('^\d+(\.\d{1,2})?$', value):  # To match only numbers and up to two decimal places
        raise ValidationError('Invalid expense format. Only numeric values are allowed.')


class WorkProgress(models.Model):
    sno= models.AutoField(primary_key=True)
    name_of_site= models.CharField(max_length=100, validators=[validate_only_letters])
    location=models.CharField(max_length=100, validators=[validate_only_letters])
    name_of_the_employee = models.CharField(max_length=100, validators=[validate_only_letters])
    phone_number = models.CharField(max_length=10, validators=[validate_mobile_number])
    to_day_expensives = models.CharField(max_length=10, validators=[validate_expenses])  
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket #{self.sno} - {self.name_of_the_employee}'
    


    from django.db import models

class Employee(models.Model):
    mobile_number = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)  # To track approval status

    def __str__(self):
        return self.mobile_number
    


    
class contract_deal(models.Model):
    name= models.CharField(max_length=100, validators=[validate_only_letters])
    phone_number = models.CharField(max_length=10, validators=[validate_mobile_number])
    contract_deal = models.CharField(max_length=100,)
    location=models.CharField(max_length=100,)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Ticket #{self.name} - {self.phone_number}'
    

    
































    
    
    name = models.CharField(max_length=255)
    contract_type = models.CharField(max_length=20)
    mobile_number = models.CharField(max_length=15)
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.contract_type}"



