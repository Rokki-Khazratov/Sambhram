from django.urls import path    
from .views import JobListCreateAPIView, JobRetrieveUpdateAPIView, ApplicationListCreateAPIView, ApplicationRetrieveUpdateAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView.as_view(), name='job-list-create'),
    path('jobs/<int:pk>/', JobRetrieveUpdateAPIView.as_view(), name='job-retrieve-update'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    path('applications/<int:pk>/', ApplicationRetrieveUpdateAPIView.as_view(), name='application-retrieve-update'),
]
