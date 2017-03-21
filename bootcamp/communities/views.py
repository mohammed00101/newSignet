from django.shortcuts import render , HttpResponse
from  .models import Community
from  django.http import JsonResponse
# Create your views here.
from .serializers import CommunitySerializerTree
from rest_framework.generics import ListAPIView

#class CommunitySerializer(serializers.):

class CommunityListAPIView(ListAPIView):
    queryset =(Community.objects.get(name='Community'),)
    serializer_class = CommunitySerializerTree
