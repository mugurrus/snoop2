# Generated by Django 2.0 on 2018-04-24 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0019_auto_20180301_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='log',
            field=models.TextField(blank=True),
        ),
    ]