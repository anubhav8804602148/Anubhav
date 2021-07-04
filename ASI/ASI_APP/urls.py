from django.conf.urls import url
from . import views

urlpatterns = [
  url('search/', views.home),
  url('',views.default),

]