from django.urls import path
from . import views

urlpatterns = [
    path("init", views.init, name="init"),
    path("continue", views.continue_query, name='continue'),
    path("get-tests", views.get_tests, name='get_tests'),
    path('appoint', views.set_specialist, name='set_specialist'),
    path('get-patient-data', views.get_patient_data, name='get_patient_data'),
    path('randomize', views.randomize, name='randomize')
]