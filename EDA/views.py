from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv, io
from .forms import *

def home(request):
	template = 'EDA/dashboard.html'
	if request.method == 'GET':
		return render(request, template)
	csv_file = request.FILES['file']
	data_set = csv_file.read().decode('UTF-8')
	print(data_set)
	io_string = io.StringIO(data_set)
	df = pd.read_csv(io_string, sep=",")
	df.to_csv(r"C:\Users\OBAID\OneDrive\Desktop\MP\EDA\file1.csv")
	print(io_string.read())
	# initialize list of lists
	# Create the pandas DataFrame 
	return render(request, template)

def BarPlotFormPage(request):
	form = BarPlotForm()
	if request.method == 'POST':
		form = BarPlotForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'EDA/bar_plot_form.html', context)

def ScatterPlotFormPage(request):
	form = ScatterPlotForm()
	if request.method == 'POST':
		form = ScatterPlotForm(request.POST)
		if form.is_valid():
			form.save()

	context = {'form':form}
	return render(request, 'EDA/scatter_plot_form.html', context)