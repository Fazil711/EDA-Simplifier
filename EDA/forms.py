from .models import BarPlotModel
from django.forms import ModelForm

class BarPlotForm(ModelForm):
	class Meta:
		model = BarPlotModel
		fields = '__all__'