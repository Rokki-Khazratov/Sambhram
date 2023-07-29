import random
import string
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Message,Content
from .serializers import MessageSerializer,ContentSerializer


class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def generate_random_slug(self):
        length = 8
        chars = string.ascii_letters + string.digits
        slug = ''.join(random.choice(chars) for _ in range(length))
        return slug

    def perform_create(self, serializer):
        slug = self.generate_random_slug()
        serializer.save(slug=slug)

class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'slug'


class MarkAsReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk' 

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ContentListCreateView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field = 'slug'