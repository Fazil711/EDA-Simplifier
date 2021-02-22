from django.db import models
import pandas as pd

# Create your models here.
class BarPlotModel(models.Model):
	df = pd.read_csv('EDA/diamonds.csv')
	single_list = df.columns
	big_list = []
	for i in single_list:
		if i != 'Unnamed: 0':
			big_list.append(tuple([i, i]))
	feature_tuple = tuple(big_list)
	print(feature_tuple)
	estimator_tuple = (
		('mean', 'mean'),
		('median', 'median'),
		)
	name = 'Bar Plot'
	x = models.CharField(max_length=200, null=True, choices=feature_tuple)
	y = models.CharField(max_length=200, null=True, choices=feature_tuple)
	hue = models.CharField(max_length=200, null=True, choices=feature_tuple, blank=True)
	estimator = models.CharField(max_length=200, default='mean', blank=True, choices=estimator_tuple)
	saturation = models.FloatField(max_length=200, null=True, blank=True) #0 to 1 1 = dark
	errcolor = models.CharField(max_length=200, default='0.26', blank=True) #0 to 1 1 = white
	errwidth = models.FloatField(max_length=200, null=True, blank=True) # 1-3 recomm
	capsize = models.FloatField(max_length=200, null=True, blank=True) # 0 to 0.4 recomm
	color = models.CharField(max_length=200, null=True, blank=True)
	n_boot = models.IntegerField(null=True, blank=True) # number of iter to cal conf int
	
	def __str__(self):
		return self.name