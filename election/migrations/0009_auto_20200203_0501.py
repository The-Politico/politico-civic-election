# Generated by Django 3.0.2 on 2020-02-03 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0008_auto_20200203_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='electiondataurl',
            name='url_descriptor',
            field=models.SlugField(max_length=25),
        ),
    ]