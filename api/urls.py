from django.urls import path    
from .views import JobListCreateAPIView, JobRetrieveUpdateAPIView, ApplicationListCreateAPIView, ApplicationRetrieveUpdateAPIView

urlpatterns = [
    path('jobs/', JobListCreateAPIView  .as_view(), name='job-list-create'),
    path('jobs/<int:id>/', JobRetrieveUpdateAPIView.as_view(), name='job-retrieve-update'),
    path('applications/', ApplicationListCreateAPIView.as_view(), name='application-list-create'),
    #query params:
    # is_hired = True/False
    # birth_range = 1990-2000
    # gender = male/female
    # first_name/last_name = STR
    # job = STR
    path('applications/<int:id>/', ApplicationRetrieveUpdateAPIView.as_view(), name='application-retrieve-update'),
]
