import uuid

from django.shortcuts import render

from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters

from django_filters.rest_framework import DjangoFilterBackend

from .serializers import AttachmentSerializer,CommentSerializer

from .utils import generate_captcha
from .models import Captcha, Comment


class AttachmentUploadView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = AttachmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status =400)

class CaptchaView(APIView):
    def get(self,request):
        text, image_file = generate_captcha()
        key = uuid.uuid4().hex[:10]
        captcha = Captcha.objects.create(key=key, text=text,image=image_file)
        return Response(
            {
                'captcha_key':key,
                'image_url': captcha.image.url
            }
        )

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.filter(parent=None).order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email', 'created_at']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context


class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.filter(parent=None).order_by('-created_at')
    serializer_class = CommentSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['username', 'email', 'created_at']
    ordering = ['-created_at']
