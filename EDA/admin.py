from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BarPlotModel)
admin.site.register(ScatterPlotModel)
admin.site.register(LinePlotModel)