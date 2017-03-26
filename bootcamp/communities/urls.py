from django.conf.urls import url
from bootcamp.communities import views

urlpatterns = [
    url(r'^$', views.CommunityListAPIView.as_view(), name='communities'),
]
