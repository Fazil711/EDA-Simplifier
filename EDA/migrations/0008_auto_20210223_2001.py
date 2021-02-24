# Generated by Django 3.1.4 on 2021-02-23 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0007_auto_20210222_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinePlotModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('y', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('hue', models.CharField(blank=True, choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('estimator', models.CharField(choices=[('mean', 'mean'), ('median', 'median')], default='none', max_length=200)),
                ('style', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('size', models.CharField(choices=[('carat', 'carat'), ('cut', 'cut'), ('color', 'color'), ('clarity', 'clarity'), ('depth', 'depth'), ('table', 'table'), ('price', 'price'), ('x', 'x'), ('y', 'y'), ('z', 'z')], max_length=200, null=True)),
                ('n_boot', models.IntegerField(blank=True, null=True)),
                ('ci', models.IntegerField(default=95)),
                ('sort', models.CharField(choices=[('True', 'True'), ('False', 'False')], default='False', max_length=200)),
                ('err_style', models.CharField(choices=[('band', 'band'), ('bar', 'bar')], default='band', max_length=200)),
                ('legend', models.CharField(choices=[('auto', 'auto'), ('brief', 'brief'), ('full', 'full'), (False, False)], default='auto', max_length=200)),
                ('palette', models.CharField(blank=True, choices=[('rocket', 'rocket'), ('mako', 'mako'), ('flare', 'flare'), ('crest', 'crest'), ('magma', 'magma'), ('viridis', 'viridis'), ('icefire', 'icefire'), ('inferno', 'inferno'), ('hot', 'hot')], max_length=200, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='scatterplotmodel',
            old_name='sizes',
            new_name='size',
        ),
        migrations.AddField(
            model_name='barplotmodel',
            name='ci',
            field=models.IntegerField(default=95),
        ),
        migrations.AddField(
            model_name='scatterplotmodel',
            name='ci',
            field=models.IntegerField(default=95),
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='saturation',
            field=models.FloatField(blank=True, null=True),
        ),
    ]