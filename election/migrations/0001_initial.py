# Generated by Django 2.0.1 on 2018-01-05 20:32

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geography', '0006_auto_20180105_2029'),
        ('government', '0003_auto_20180105_2032'),
        ('entity', '0002_auto_20180105_2022'),
    ]

    operations = [
        migrations.CreateModel(
            name='BallotAnswer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('answer', models.TextField()),
                ('winner', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='BallotMeasure',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('question', models.TextField()),
                ('number', models.CharField(max_length=3)),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ballot_measures', to='geography.Division')),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('ap_candidate_id', models.CharField(max_length=255)),
                ('incumbent', models.BooleanField(default=False)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidates', to='government.Party')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidacies', to='entity.Person')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateElection',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('aggregable', models.BooleanField(default=True)),
                ('uncontested', models.BooleanField(default=False)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_elections', to='election.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('candidates', models.ManyToManyField(through='election.CandidateElection', to='election.Candidate')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elections', to='geography.Division')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionCycle',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=10, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=4, unique=True)),
                ('name', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='ElectionDay',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('date', models.DateField(unique=True)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elections_days', to='election.ElectionCycle')),
            ],
        ),
        migrations.CreateModel(
            name='ElectionType',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('ap_code', models.CharField(max_length=1)),
                ('is_general', models.BooleanField(default=False)),
                ('primary_type', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_winners', models.PositiveSmallIntegerField(default=1)),
                ('winning_threshold', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('uid', models.CharField(blank=True, editable=False, max_length=500, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('label', models.CharField(blank=True, max_length=255)),
                ('short_label', models.CharField(blank=True, max_length=50, null=True)),
                ('special', models.BooleanField(default=False)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='races', to='election.ElectionCycle')),
                ('office', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='races', to='government.Office')),
            ],
        ),
        migrations.AddField(
            model_name='election',
            name='election_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elections', to='election.ElectionDay'),
        ),
        migrations.AddField(
            model_name='election',
            name='election_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elections', to='election.ElectionType'),
        ),
        migrations.AddField(
            model_name='election',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='government.Party'),
        ),
        migrations.AddField(
            model_name='election',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='elections', to='election.Race'),
        ),
        migrations.AddField(
            model_name='candidateelection',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_elections', to='election.Election'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='race',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='candidates', to='election.Race'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='top_of_ticket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ticket', to='election.Candidate'),
        ),
        migrations.AddField(
            model_name='ballotmeasure',
            name='election_day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='ballot_measures', to='election.ElectionDay'),
        ),
        migrations.AddField(
            model_name='ballotanswer',
            name='ballot_measure',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='election.BallotMeasure'),
        ),
        migrations.AlterUniqueTogether(
            name='candidateelection',
            unique_together={('candidate', 'election')},
        ),
    ]
