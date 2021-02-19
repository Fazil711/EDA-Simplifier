from . import views
from django.urls import path
from . import csvaccept

urlpatterns = [
    path('', views.home),
]