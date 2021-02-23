from django.db import models
import pandas as pd

def accept_csv():
	df = pd.read_csv('EDA/diamonds.csv')
	return df

def estimator_tuples():
	estimator_tuple = (
		('mean', 'mean'),
		('median', 'median'),
		)
	return estimator_tuple

def feature_tuples(df):
	single_list = df.columns
	big_list = []
	for i in single_list:
		if i != 'Unnamed: 0':
			big_list.append(tuple([i, i]))
	feature_tuple = tuple(big_list)
	return feature_tuple

def palette_choices():
	palette_choice = (
		('rocket', 'rocket'),
		('mako', 'mako'),
		('flare', 'flare'),
		('crest', 'crest'),
		('magma', 'magma'),
		('viridis', 'viridis'),
		('icefire', 'icefire'),
		('inferno', 'inferno'),
		('hot', 'hot'),
		)
	return palette_choice

def legend_choices():
	legend_choice = (
		('auto', 'auto'),
		('brief', 'brief'),
		('full', 'full'),
		(False, False),
		)
	return legend_choice

def bool_choices():
	bool_choice = (
		('True', 'True'),
		('False', 'False'),
		)
	return bool_choice

# Create your models here.
class BarPlotModel(models.Model):
	df = accept_csv()
	name = 'Bar Plot'
	x = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	y = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	hue = models.CharField(max_length=200, null=True, choices=feature_tuples(df), blank=True)
	estimator = models.CharField(max_length=200, default='mean', blank=True, choices=estimator_tuples())
	saturation = models.FloatField(null=True, blank=True) #0 to 1 1 = dark
	errcolor = models.CharField(max_length=200, default='0.26', blank=True) #0 to 1 1 = white
	errwidth = models.FloatField(max_length=200, null=True, blank=True) # 1-3 recomm
	capsize = models.FloatField(max_length=200, null=True, blank=True) # 0 to 0.4 recomm
	color = models.CharField(max_length=200, null=True, blank=True)
	n_boot = models.IntegerField(null=True, blank=True) # number of iter to cal conf int
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	ci = models.IntegerField(default=95)
	
	def __str__(self):
		return 'Bar Plot'

class ScatterPlotModel(models.Model):
	df = accept_csv()
	name = 'Scatter Plot'
	x = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	y = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	hue = models.CharField(max_length=200, null=True, choices=feature_tuples(df), blank=True)
	estimator = models.CharField(max_length=200, default='none', choices=estimator_tuples())
	style = models.CharField(max_length=200, null=True, choices=feature_tuples(df)) #Different shapes of scattered points
	size = models.CharField(max_length=200, null=True, choices=feature_tuples(df)) #Different sizes of scattered points
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	legend = models.CharField(max_length=200, default='auto', choices=legend_choices())
	n_boot = models.IntegerField(null=True, blank=True) # number of iter to cal conf int
	ci = models.IntegerField(default=95)
	
	def __str__(self):
		return 'Scatter Plot'

class LinePlotModel(models.Model):
	df = accept_csv()
	err_style_choices = (
		('band', 'band'),
		('bar', 'bar'),
		)
	name = 'Line Plot'
	x = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	y = models.CharField(max_length=200, null=True, choices=feature_tuples(df))
	hue = models.CharField(max_length=200, null=True, choices=feature_tuples(df), blank=True)
	estimator = models.CharField(max_length=200, default='none', choices=estimator_tuples())
	style = models.CharField(max_length=200, null=True, choices=feature_tuples(df)) #Different shapes of scattered points
	size = models.CharField(max_length=200, null=True, choices=feature_tuples(df)) #Different sizes of scattered points
	n_boot = models.IntegerField(null=True, blank=True) # number of iter to cal conf int
	ci = models.IntegerField(default=95) 
	sort = models.CharField(max_length=200, default='False', choices=bool_choices()) # Sort Values, default is False
	err_style = models.CharField(max_length=200, default='band', choices=err_style_choices)
	legend = models.CharField(max_length=200, default='auto', choices=legend_choices())
	palette = models.CharField(max_length=200, blank=True, null=True, choices=palette_choices())
	
	def __str__(self):
		return 'Line Plot'