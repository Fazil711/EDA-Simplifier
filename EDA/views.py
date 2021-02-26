from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv, io
from .forms import *
from .models import *
from os.path import dirname, abspath

def make_graph(a, num):
	df = pd.read_csv('EDA/Diamonds.csv')
	li = []
	j = 1
	for i in a:
		j += 1
		if(a[i]==''):
			li.append(None)
		else:
			li.append(a[i])
	if(num == 1):
		li[6] = float(li[6])
		li[6] = max(min(1, li[6]), 0)
		li[8] = float(li[8])
		li[8] = max(min(3, li[8]), 1)
		li[9] = float(li[9])
		li[9] = max(min(0.4, li[9]), 0)
		li[11] = int(li[11])
		li[11] = max(1, li[11])
		li[13] = int(li[13])
		li[13] = max(min(100, li[13]), 1)
		plot = sns.barplot(x=str(li[2]), y=str(li[3]), hue=li[4], saturation=float(li[6]), errcolor=li[7], 
			errwidth=float(li[8]), capsize=float(li[9]), color=li[10], n_boot=int(li[11]), palette=li[12], ci=int(li[13]), 
			data=df)
		fig = plot.get_figure()
		d = dirname(dirname(abspath(__file__))) # /home/kristina/desire-directory
		d += '\static\images\output.png'
		fig.savefig(d)

def home(request):
	template = 'EDA/dashboard.html'
	if request.method == 'GET':
		return render(request, template)
	csv_file = request.FILES['file']
	data_set = csv_file.read().decode('UTF-8')
	print(data_set)
	io_string = io.StringIO(data_set)
	df = pd.read_csv(io_string, sep=",")
	df.to_csv(r"C:\Users\OBAID\OneDrive\Desktop\EDA-Simplifier\EDA\file1.csv")
	print(io_string.read())
	# initialize list of lists
	# Create the pandas DataFrame 
	return render(request, template)

def BarPlotFormPage(request):
	form = BarPlotForm()
	if request.method == 'POST':
		form = BarPlotForm(request.POST)
		if form.is_valid():
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 1)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/bar_plot_form.html', context)

def ScatterPlotFormPage(request):
	form = ScatterPlotForm()
	if request.method == 'POST':
		form = ScatterPlotForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/scatter_plot_form.html', context)

def LinePlotFormPage(request):
	form = LinePlotForm()
	if request.method == 'POST':
		form = LinePlotForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/line_plot_form.html', context)

def BoxPlotFormPage(request):
	form = BoxPlotForm()
	if request.method == 'POST':
		form = BoxPlotForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/box_plot_form.html', context)

def CountPlotFormPage(request):
	form = CountPlotForm()
	if request.method == 'POST':
		form = CountPlotForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/count_plot_form.html', context)

def HistogramPlotFormPage(request):
	form = HistogramPlotForm()
	if request.method == 'POST':
		form = HistogramPlotForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/histogram_plot_form.html', context)

def deleteGraph(request):
	graph = BarPlotModel.objects.get(name= 'Bar Plot')
	if request.method == "POST" :
		graph.delete()
		return redirect('/')

	context = {'graph':graph}
	return render(request, 'EDA/forms/delete_form.html', context)