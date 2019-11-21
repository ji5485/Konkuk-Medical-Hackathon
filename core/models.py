from django.db import models
from django.contrib.auth.models import User

class MedicalDepartment(models.Model):
    name = models.CharField(max_length=30)
    base_fare = models.IntegerField()

    def __str__(self):
        return self.name

class SelfDiagnosis(models.Model):
    department = models.ForeignKey(MedicalDepartment, on_delete=models.CASCADE)
    opinion = models.TextField(null=True)
    is_visited = models.BooleanField(null=True)
    is_rediagnose = models.BooleanField(null=True)
    medicine = models.TextField(null=True)

class Symtom(models.Model):
    self_diagnosis = models.ForeignKey(SelfDiagnosis, on_delete=models.CASCADE)
    name = models.OneToOneField("Disease", on_delete=models.CASCADE)
    period = models.TextField()
    degree = models.IntegerField()

    def __str__(self):
        return self.name

# TODO: Treatment 에 급여 비급여 나눠야할까?
class Treatment(models.Model):
    department = models.ManyToManyField(MedicalDepartment)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Disease(models.Model):
    # name 과 code 크롤링해서 price table과 join 후 db 에 넣기
    department = models.ManyToManyField(MedicalDepartment)
    name = models.CharField(max_length=30)
    code = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
