# Generated by Django 3.1.4 on 2021-02-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0006_auto_20210222_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScatterPlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('y', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('hue', models.CharField(blank=True, choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('estimator', models.CharField(choices=[('mean', 'mean'), ('median', 'median')], default='none', max_length=200)),
                ('style', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('sizes', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('palette', models.CharField(blank=True, choices=[('rocket', 'rocket'), ('mako', 'mako'), ('flare', 'flare'), ('crest', 'crest'), ('magma', 'magma'), ('viridis', 'viridis'), ('icefire', 'icefire'), ('inferno', 'inferno'), ('hot', 'hot')], max_length=200, null=True)),
                ('legend', models.CharField(choices=[('auto', 'auto'), ('brief', 'brief'), ('full', 'full'), (False, False)], default='auto', max_length=200)),
                ('n_boot', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='barplotmodel',
            name='palette',
            field=models.CharField(blank=True, choices=[('rocket', 'rocket'), ('mako', 'mako'), ('flare', 'flare'), ('crest', 'crest'), ('magma', 'magma'), ('viridis', 'viridis'), ('icefire', 'icefire'), ('inferno', 'inferno'), ('hot', 'hot')], max_length=200, null=True),
        ),
    ]