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

def save_graph(plot):
	fig = plot.get_figure()
	d = dirname(dirname(abspath(__file__)))
	d += '\static\images\cc.png'
	fig.savefig(d)

def make_graph(a, num):
	df = pd.read_csv('EDA/Diamonds.csv')
	li, j = [], 1
	for i in a:
		j += 1
		if(a[i]==''):
			li.append(None)
		else:
			li.append(a[i])
	print(a)
	print(li)

	if(num == 1):
		li[5] = max(min(1, float(li[5])), 0)
		li[7] = max(min(3, float(li[7])), 1)
		li[8] = max(min(0.4, float(li[8])), 0)
		li[10] = max(1, int(li[10]))
		li[12] = max(min(99, int(li[12])), 1)
		plot = sns.barplot(x=str(li[2]), y=str(li[3]), hue=li[4], saturation=li[5], errcolor=li[6], 
			errwidth=li[7], capsize=li[8], color=li[9], n_boot=li[10], palette=li[11], ci=li[12], 
			data=df)
		save_graph(plot)	

	if(num == 2):
		li[10] = min(99, max(1, int(li[10])))
		plot = sns.scatterplot(x=li[2], y=li[3], hue=li[4], style=li[5], size=li[6], 
			palette=li[7], legend=li[8], n_boot=li[9], ci=li[10], data=df)
		save_graph(plot)

	if(num == 3):
		li[8] = min(99, max(1, int(li[8])))
		if(li[9] == 'False'):
			li[9] = bool(li[9])
			li[9] = False
		else:
			li[9] = bool(li[9])
			li[9] = True
		plot = sns.lineplot(x=li[2], y=li[3], hue=li[4], style=li[5], size=li[6],
			n_boot=li[7], ci=li[8], sort=li[9], err_style=li[10], legend=li[11], palette=li[12],
			data=df)
		save_graph(plot)

	if(num == 4):
		li[4] = min(1, max(0, float(li[4])))
		plot = sns.countplot(x=li[2], hue=li[3], saturation=li[4], palette=li[5], dodge=li[6],
			data=df)
		save_graph(plot)

	if(num == 5):
		if(li[5] != 'auto'):
			li[5] = int(li[5])
		if(li[7]=='True'):
			li[7] = True
		else:
			li[7] = False
		if(li[10]=='True'):
			li[10] = True
		else:
			li[10] = False
		if(li[11]=='True'):
			li[11] = True
		else:
			li[11] = False
		plot = sns.histplot(x=li[2], hue=li[3], stat=li[4], bins=li[5],binwidth=li[6], 
			discrete=li[7], palette=li[8], legend=li[9], fill=li[10], kde=li[11], multiple=li[12], 
			element=li[13], data=df)
		save_graph(plot)

	if(num == 6):
		if(li[8]=='True'):
			li[8] = True
		else:
			li[8] = False
		li[5] = min(1, max(0, float(li[5])))
		li[7] = float(li[7])
		li[9] = float(li[9])
		plot = sns.boxplot(x=li[2], y=li[3], hue=li[4], saturation=li[5], palette=li[6], width=li[7],
			dodge=li[8], fliersize=li[9], linewidth=li[10], data=df)
		save_graph(plot)

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
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 2)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/scatter_plot_form.html', context)

def LinePlotFormPage(request):
	form = LinePlotForm()
	if request.method == 'POST':
		form = LinePlotForm(request.POST)
		if form.is_valid():
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 3)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/line_plot_form.html', context)

def CountPlotFormPage(request):
	form = CountPlotForm()
	if request.method == 'POST':
		form = CountPlotForm(request.POST)
		if form.is_valid():
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 4)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/count_plot_form.html', context)

def HistogramPlotFormPage(request):
	form = HistogramPlotForm()
	if request.method == 'POST':
		form = HistogramPlotForm(request.POST)
		if form.is_valid():
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 5)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/histogram_plot_form.html', context)

def BoxPlotFormPage(request):
	form = BoxPlotForm()
	if request.method == 'POST':
		form = BoxPlotForm(request.POST)
		if form.is_valid():
			#form.save()
			context = {'form':form}
			#return render(request, 'EDA/BarPlotFormPage.html', context)
			make_graph(request.POST, 6)
			#form.delete()
			return redirect('/')

	context = {'form':form}
	return render(request, 'EDA/forms/box_plot_form.html', context)

def deleteGraph(request):
	graph = BarPlotModel.objects.get(name= 'Bar Plot')
	if request.method == "POST" :
		graph.delete()
		return redirect('/')

	context = {'graph':graph}
	return render(request, 'EDA/forms/delete_form.html', context)