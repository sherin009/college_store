from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=20)
    mail_id = models.EmailField()
    address = models.CharField(max_length=255)
    department = models.CharField(max_length=100)
    courses = models.CharField(max_length=100)
    purpose = models.CharField(max_length=100)

    def __str__(self):
        return self.name
