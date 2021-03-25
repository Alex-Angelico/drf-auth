from jets.permissions import IsOwnerOrReadOnly
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import JetsSerializer
from .models import Jets

class JetsListView(generics.ListCreateAPIView):
  permission_classes = (IsAuthenticatedOrReadOnly,)
  queryset = Jets.objects.all()
  serializer_class = JetsSerializer

class JetsDetailView(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly,)
  queryset = Jets.objects.all()
  serializer_class = JetsSerializer