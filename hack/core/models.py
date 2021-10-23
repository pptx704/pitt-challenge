from django.db import models
from .utils import sex_choice
from uuid import uuid4

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    sex = models.CharField(choices=sex_choice, max_length=7)
    address = models.CharField(max_length=256, null=True, blank=True)
    specialist = models.ForeignKey('Specialist', related_name='patients', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class Specialist(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Diagnosis(models.Model):
    name = models.CharField(max_length=64)
    patient = models.ForeignKey(Patient, related_name='diagnosis', on_delete=models.CASCADE)
    value = models.FloatField()
    Specialist = models.ForeignKey(Specialist, related_name='diagnosis', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

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