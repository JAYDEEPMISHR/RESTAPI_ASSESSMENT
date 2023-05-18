from django.shortcuts import render
from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer

# Create your views here.

class Snippetlist(generics.ListCreateAPIView):
	queryset=Snippet.objects.all()
	serializer_class=SnippetSerializer

class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Snippet
	serializer_class=SnippetSerializer