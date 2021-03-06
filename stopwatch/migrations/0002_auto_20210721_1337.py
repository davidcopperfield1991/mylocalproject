# Generated by Django 3.2.3 on 2021-07-21 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stopwatch', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='timedetail',
            options={'verbose_name': 'stopwatch', 'verbose_name_plural': 'stopwatch'},
        ),
        migrations.AlterField(
            model_name='timedetail',
            name='start_time',
            field=models.TimeField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='timedetail',
            name='stop_time',
            field=models.TimeField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='timedetail',
            name='totla_time',
            field=models.TimeField(blank=True, default=0),
        ),
    ]
