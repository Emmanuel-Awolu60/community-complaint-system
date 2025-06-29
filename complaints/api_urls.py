from django.urls import path
from .views import ComplaintDetailAPIView, ComplaintDetailAPIView

urlpatterns =[
    path('complaints/', ComplaintDetailAPIView.as_view(), name='api_complaints'),
    path('complaint/<int:pk>/', ComplaintDetailAPIView.as_view(), name='api_complaint_detail')
]