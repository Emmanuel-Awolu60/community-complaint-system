from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.sub, name= 'submit_comlaint'),
]

