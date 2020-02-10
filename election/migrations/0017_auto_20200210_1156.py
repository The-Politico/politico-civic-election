# Generated by Django 3.0.3 on 2020-02-10 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('election', '0016_candidateelection_ap_candidate_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='ap_candidate_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='AP candidate ID'),
        ),
        migrations.AlterField(
            model_name='candidateelection',
            name='ap_candidate_number',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='AP candidate number'),
        ),
        migrations.AlterField(
            model_name='electionevent',
            name='election_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='election_events', to='election.ElectionDay'),
        ),
    ]
