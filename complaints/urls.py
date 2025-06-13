from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('submitted/', views.complaint_submitted, name='complaint_submitted'),
    path('list/', views.complaint_list, name='complaint_list'),
    path('upvote/<int:complaint_id>/', views.upvote_complaint, name='upvote_complaint'),
]
