from django.contrib import admin
from .models import (
    Patient,
    Evidence,
    Inferma,
    Doctor,
    Diagnostic,
    Test
)
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

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_filter = ['department', 'city']
    search_fields = ['name']

@admin.register(Diagnostic)
class DiagnosticAdmin(admin.ModelAdmin):
    pass

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    pass