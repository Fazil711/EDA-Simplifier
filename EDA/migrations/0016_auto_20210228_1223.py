# Generated by Django 3.1.4 on 2021-02-28 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EDA', '0015_auto_20210226_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barplotmodel',
            name='estimator',
        ),
        migrations.RemoveField(
            model_name='boxplotmodel',
            name='estimator',
        ),
        migrations.RemoveField(
            model_name='countplotmodel',
            name='estimator',
        ),
        migrations.RemoveField(
            model_name='lineplotmodel',
            name='estimator',
        ),
        migrations.RemoveField(
            model_name='scatterplotmodel',
            name='estimator',
        ),
        migrations.AlterField(
            model_name='barplotmodel',
            name='capsize',
            field=models.FloatField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
