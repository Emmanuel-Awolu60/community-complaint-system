from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_complaint, name='submit_complaint'),
    path('submitted/', views.complaint_submitted, name='complaint_submitted'),
    path('list/', views.complaint_list, name='complaint_list'),
    path('upvote/<int:complaint_id>/', views.upvote_complaint, name='upvote_complaint'),

    # REST API endpoints
    path('api/complaints/', views.ComplaintListCreateAPIView.as_view(), name='complaint-list-create'),
    path('api/complaints/<int:pk>/', views.ComplaintDetailAPIView.as_view(), name='complaint-detail'),
]
