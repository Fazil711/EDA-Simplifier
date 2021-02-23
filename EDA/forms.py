from .models import *
from django.forms import ModelForm

class BarPlotForm(ModelForm):
	class Meta:
		model = BarPlotModel
		fields = '__all__'

class ScatterPlotForm(ModelForm):
	class Meta:
		model = ScatterPlotModel
		fields = '__all__'

class LinePlotForm(ModelForm):
	class Meta:
		model = LinePlotModel
		fields = '__all__'