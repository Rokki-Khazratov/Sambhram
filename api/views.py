from rest_framework import generics
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer
from datetime import datetime

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

from rest_framework import generics
from .models import Application
from .serializers import ApplicationSerializer
from datetime import datetime

class ApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        is_hired = self.request.query_params.get('is_hired', None)
        first_validation = self.request.query_params.get('first_validation', None)
        second_validation = self.request.query_params.get('second_validation', None)
        birth_range = self.request.query_params.get('birth_range', None)
        gender = self.request.query_params.get('gender', None)
        job_title = self.request.query_params.get('job_title', None)
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        queryset = Application.objects.all()

        
        if queryset == queryset.filter(first_validation=True):
            print(queryset.filter(first_validation=True))
        else :
            print(queryset.filter(first_validation=False))

        if is_hired is not None:
            is_hired = bool(is_hired)
            queryset = queryset.filter(is_hired=is_hired)

        if first_validation is not None:
            queryset = queryset.filter(first_validation=first_validation)

        if second_validation is not None:
            queryset = queryset.filter(second_validation=second_validation)

        if birth_range is not None:
            try:
                start_date_str, end_date_str = birth_range.split('-')
                start_date = datetime.strptime(start_date_str, '%Y')
                end_date = datetime.strptime(end_date_str, '%Y')
                queryset = queryset.filter(birth_date__range=(start_date, end_date))
            except ValueError:
                pass

        if gender is not None:
            gender = gender.lower()
            if gender == 'male':
                queryset = queryset.filter(gender='M')
            elif gender == 'female':
                queryset = queryset.filter(gender='F')

        if job_title is not None:
            queryset = queryset.filter(job__title=job_title)

        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset


    serializer_class = ApplicationSerializer

    def get_queryset(self):
        is_hired = self.request.query_params.get('is_hired', None)
        first_validation = self.request.query_params.get('first_validation', None)
        second_validation = self.request.query_params.get('second_validation', None)
        birth_range = self.request.query_params.get('birth_range', None)
        gender = self.request.query_params.get('gender', None)
        job_title = self.request.query_params.get('job_title', None)
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        queryset = Application.objects.all()

        if is_hired is not None:
            is_hired = bool(is_hired)
            queryset = queryset.filter(is_hired=is_hired)

        if first_validation is not None:
            first_validation = bool(first_validation) 
            queryset = queryset.filter(first_validation=first_validation)

        if second_validation is not None:
            second_validation = bool(second_validation)
            queryset = queryset.filter(second_validation=second_validation)


        if birth_range is not None:
            try:
                start_date_str, end_date_str = birth_range.split('-')
                start_date = datetime.strptime(start_date_str, '%Y')
                end_date = datetime.strptime(end_date_str, '%Y')
                queryset = queryset.filter(birth_date__range=(start_date, end_date))
            except ValueError:
                pass

        if gender is not None:
            gender = gender.lower()
            if gender == 'male':
                queryset = queryset.filter(gender='M')
            elif gender == 'female':
                queryset = queryset.filter(gender='F')

        if job_title is not None:
            queryset = queryset.filter(job__title=job_title)

        if first_name is not None:
            queryset = queryset.filter(name__icontains=first_name)

        if last_name is not None:
            queryset = queryset.filter(surname__icontains=last_name)

        return queryset

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'

class ApplicationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ApplicationSerializer

    def get_queryset(self):
        is_hired = self.request.query_params.get('is_hired', None)
        birth_range = self.request.query_params.get('birth_range', None)
        gender = self.request.query_params.get('gender', None)
        job_title = self.request.query_params.get('job_title', None)
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        queryset = Application.objects.all()

        if is_hired is not None:
            is_hired = is_hired.lower()
            if is_hired == 'true':
                queryset = queryset.filter(is_hired=True)
            elif is_hired == 'false':
                queryset = queryset.filter(is_hired=False)

        if birth_range is not None:
            try:
                start_date_str, end_date_str = birth_range.split('-')
                start_date = datetime.strptime(start_date_str, '%Y')
                end_date = datetime.strptime(end_date_str, '%Y')
                queryset = queryset.filter(birth_date__range=(start_date, end_date))
            except ValueError:
                pass

        if gender is not None:
            gender = gender.lower()
            if gender == 'male':
                queryset = queryset.filter(gender='M')
            elif gender == 'female':
                queryset = queryset.filter(gender='F')

        if job_title is not None:
            queryset = queryset.filter(job__title=job_title)

        if first_name is not None:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name is not None:
            queryset = queryset.filter(last_name__icontains=last_name)

        return queryset


class ApplicationRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'id'