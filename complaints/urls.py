from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.sub, name= 'submit_comlaint'),
    path('submitted/', views.complaint_submitted, name='complaint_submitted'),
    path('list/', views.comlaint_list, name='complaint_list')
]

