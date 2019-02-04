from django.conf.urls import url 
from .views import FirstView, StartView

urlpatterns = [
  url(r'^first/$', FirstView.as_view(), name="first"),
  url(r'^start/$', StartView.as_view(), name="start"),
]
