from django.db import models

# Create your models here.
from django.db import models


class District(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Branch(models.Model):
    name = models.CharField(max_length=50)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Registration(models.Model):
    Gender_Choices =[
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10,choices=Gender_Choices)
    dob = models.DateField()
    address = models.TextField()
    mob_no = models.IntegerField()
    mail_id = models.EmailField()
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=20)
    book = models.BooleanField(default=False)
    pen = models.BooleanField(default=False)
    exam_papers = models.BooleanField(default=False)

    def __str__(self):
        return self.name
