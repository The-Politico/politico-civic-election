# Generated by Django 3.0.3 on 2020-02-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0017_auto_20200210_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidateelection',
            name='ballot_order',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]