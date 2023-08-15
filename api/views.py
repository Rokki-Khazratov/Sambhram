from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from datetime import datetime
from django.contrib.auth.decorators import login_required


from .models import Job, Application,User
from .serializers import JobSerializer, ApplicationSerializer,UserSerializer
from django.contrib.auth import get_user_model

import jwt
from django.conf import settings

class UserLoginAPIView(generics.GenericAPIView):
    def post(self, request):
        User = get_user_model()
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({'error': 'Пользователь не существует'}, status=status.HTTP_401_UNAUTHORIZED)

        if user.password == password:
            payload = {
                'user_id': user.id,
                'username': user.username,
            }
            token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

            # Установка куки с токеном
            response = Response({'token': token}, status=status.HTTP_200_OK)
            response.set_cookie('jwt_token', token, httponly=True, samesite='Lax')
            return response
        else:
            return Response({'error': 'Неверный пароль'}, status=status.HTTP_401_UNAUTHORIZED)










class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class JobRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_field = 'id'


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

        if is_hired is not None:
            is_hired = bool(is_hired)
            queryset = queryset.filter(is_hired=is_hired)

        if first_validation is not None:
            first_validation = first_validation.lower()
            if first_validation == 'true':
                queryset = queryset.filter(first_validation=True)
            elif first_validation == 'false':
                queryset = queryset.filter(first_validation=False)

        if second_validation is not None:
            second_validation = second_validation.lower()
            if second_validation == 'true':
                queryset = queryset.filter(second_validation=True)
            elif second_validation == 'false':
                queryset = queryset.filter(second_validation=False)

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

class ApplicationRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    lookup_field = 'id'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@login_required
def application_list(request):
    user_role = request.user.role
    if user_role == 2:  # First Admin
        applications = Application.objects.filter(first_validation=False, second_validation=False)
    elif user_role == 3:  # Second Admin
        applications = Application.objects.filter(first_validation=True, second_validation=False) 
    elif user_role == 4:  # Chief Admin
        applications = Application.objects.all(first_validation=True, second_validation=True)
    else:  # Default: Admin (role == 1)
        applications = Application.objects.all(first_validation=True, second_validation=True)  
    
    # Serialize the applications and return the response
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def apply_to_next_manager(request, application_id):
    try:
        application = Application.objects.get(pk=application_id)
        user_role = request.user.role

        if user_role == 2:
            application.first_validation = True
            application.second_validation = False
            application.is_hired = False
        elif user_role == 3:
            application.second_validation = True
            application.is_hired = False
        elif user_role == 4:
            application.is_hired = True
        else:
            return Response({"error": "You are not authorized to approve this application."}, status=403)

        application.save()
        return Response({"message": "Application approved successfully."})

    except Application.DoesNotExist:
        return Response({"error": "Application not found."}, status=404)