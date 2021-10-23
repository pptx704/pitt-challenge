from django.urls import path
from . import views

urlpatterns = [
    path("init", views.init, name="init"),
    path("continue", views.continue_query, name='continue'),
    path("get-tests", views.get_tests, name='get_tests'),
]