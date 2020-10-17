from django.shortcuts import render
from rest_framework import generics
from test.models import *
from test.serializers import *
# Create your views here.


class getCategories(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer