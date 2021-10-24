from django.db import models
from .utils import sex_choice, boroughs
from uuid import uuid4

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    sex = models.CharField(choices=sex_choice, max_length=7)
    height = models.FloatField()
    weight = models.FloatField()
    street = models.CharField(max_length=256, null=True, blank=True)
    city = models.CharField(max_length=20, choices=boroughs)
    phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name
    
    def serialize(self):
        return {
            'name': self.name,
            'age': self.age,
            'sex': self.sex,
            'height': self.height,
            'weight': self.weight,
            'phone': self.phone
        }


class Inferma(models.Model):
    patient = models.OneToOneField(Patient, related_name="inferma", on_delete=models.CASCADE)
    key = models.CharField(default=uuid4, max_length=64)

    def __str__(self) -> str:
        return self.patient.name

class Evidence(models.Model):
    inferma = models.ForeignKey(Inferma, on_delete=models.CASCADE, related_name='evidences')
    evidence_id = models.CharField(max_length=16)
    choice_id = models.CharField(max_length=7, blank=True, null=True)
    initial = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.evidence_id}: {self.inferma}"

    def serialize(self):
        data = {
            'id': self.evidence_id,
            'choice_id': self.choice_id,
        }

        if self.initial:
            data['source'] = 'initial'

        return data

class Doctor(models.Model):
    key = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    city = models.CharField(max_length=20, choices=boroughs)
    email = models.EmailField(max_length=128)

    def __str__(self):
        return f"{self.name}, {self.department.title()}, {self.city}"

class Diagnostic(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnostics')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='diagnostics')
    emergency = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.patient} - {self.doctor}"

class Test(models.Model):
    name = models.CharField(max_length=64)
    value = models.FloatField()
    unit = models.CharField(max_length=64)
    diagnostic = models.ForeignKey(Diagnostic, on_delete=models.CASCADE, related_name='tests')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.diagnostic.patient} - {self.diagnostic.doctor} - {self.time}"

    def serialize(self):
        return {
            'value': self.value,
            'unit': self.unit,
            'date': self.time.strftime("%d %b, %Y"),
            'time': self.time.strftime("%H:%M")
        }