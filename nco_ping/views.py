from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import NcoPing
from .serializers import NcoPingSerializer

class NcoPingList(generics.ListCreateAPIView):
    queryset = NcoPing.objects.all()
    serializer_class = NcoPingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
