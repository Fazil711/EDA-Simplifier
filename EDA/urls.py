from . import views
from django.urls import path
from . import csvaccept

urlpatterns = [
    path('', views.home, name='home'),
    path('bar_plot_form/', views.BarPlotFormPage, name='bar_plot_form_page'),
]