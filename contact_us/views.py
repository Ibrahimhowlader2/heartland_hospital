from rest_framework import generics,mixins,parsers,viewsets
from .models import ContactUs
from .serializers import ContactUsSerializer

# Create your views here.

class ContactUsViewSet(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer

