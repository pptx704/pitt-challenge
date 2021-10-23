from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    pass

@admin.register(Evidence)
class EvidenceAdmin(admin.ModelAdmin):
    pass

@admin.register(Inferma)
class InfermaAdmin(admin.ModelAdmin):
    pass

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    pass