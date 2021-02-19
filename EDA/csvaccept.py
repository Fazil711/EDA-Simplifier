from django.shortcuts import render
from django.contrib import messages
import csv, io
import pandas as pd

def csv_accept(request):
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