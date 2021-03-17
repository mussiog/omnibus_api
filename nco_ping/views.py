from django.shortcuts import render
from rest_framework import generics, permissions, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer

class Nco_pingList(generics.ListCreateAPIView):
    queryset = Nco_ping.objects.all()
    serializer_class = NcoPingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)


class Nco_pingRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = Nco_ping.objects.all()
    serializer_class = NcoPingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        host = Post.objects.filter(pk=kwargs['pk'])
        if post.exists():
            return self.destroy(request, *args, **kwargs)
        else:
            raise ValidationError('Host doesn\'t exist')


class Nco_pingCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    serializer_class = NcoPingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        host = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(host=host)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('host already exist on ping probe')
        serializer.save(post=Post.objects.get(pk=self.kwargs['pk']))

    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('your server doesn\'t exist')
