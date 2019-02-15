from django.conf.urls import url 
from .views import FirstView, StartView

 #appnameを追加
app_name = "themlp"

urlpatterns = [
  url(r'^first/$', FirstView.as_view(), name="first"),
  url(r'^start/$', StartView.as_view(), name="start"),
]
