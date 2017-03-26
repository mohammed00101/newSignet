from django.shortcuts import render, HttpResponse, render_to_response
from django.contrib.auth.decorators import login_required
from django.test import RequestFactory
from  django.shortcuts import render
from .models import Community
from  django.http import JsonResponse
# Create your views here.
from .serializers import CommunitySerializerTree
from rest_framework.generics import ListCreateAPIView , ListAPIView
import  json




# class CommunitySerializer(serializers.):

class CommunityListAPIView(ListCreateAPIView):
    queryset = (Community.objects.get(name='Community'),)
    serializer_class = CommunitySerializerTree
    def listJson(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CommunitySerializerTree(queryset, many=True)
        return json.dumps(serializer.data)


def pickupCommunity(request):
    com = CommunityListAPIView()
    return render(request,
                  'communities/communities.html',
                  {'community':com.listJson(request)})
