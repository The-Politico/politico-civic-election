# Generated by Django 3.0.2 on 2020-01-14 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('geography', '0003_auto_20190821_2122'),
        ('government', '0005_auto_20190826_2043'),
        ('election', '0005_race_electoral_votes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='election',
            name='division',
        ),
        migrations.RemoveField(
            model_name='election',
            name='election_day',
        ),
        migrations.RemoveField(
            model_name='election',
            name='election_type',
        ),
        migrations.RemoveField(
            model_name='election',
            name='party',
        ),
        migrations.AddField(
            model_name='electionevent',
            name='election_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='election_events', to='election.ElectionType'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='electiontype',
            name='slug',
            field=models.SlugField(blank=True, choices=[('general', 'General'), ('party-primary', 'Party Primary'), ('all-party-primary', 'All-party Primary'), ('primary-runoff', 'Primary Runoff'), ('general-runoff', 'General Runoff')], max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='electionevent',
            unique_together={('division', 'election_day', 'election_type')},
        ),
        migrations.CreateModel(
            name='ElectionBallot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(blank=True, editable=False, max_length=500)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=255, unique=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('offices_elected', models.SlugField(choices=[('president', 'Presidential race'), ('all', 'Presidential Congressional & Statewide races'), ('downticket', 'Congressional & Statewide races')], default='downticket', max_length=15)),
                ('early_vote_start', models.DateField(blank=True, null=True)),
                ('early_vote_close', models.DateField(blank=True, null=True)),
                ('vote_by_mail_application_deadline', models.DateField(blank=True, null=True)),
                ('vote_by_mail_ballot_deadline', models.DateField(blank=True, null=True)),
                ('early_voting_notes', models.TextField(blank=True, null=True)),
                ('online_registration_deadline', models.DateField(blank=True, null=True)),
                ('registration_deadline', models.DateField(blank=True, null=True)),
                ('poll_closing_time', models.DateTimeField(blank=True, null=True)),
                ('registration_notes', models.TextField(blank=True, null=True)),
                ('election_event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='election.ElectionEvent')),
                ('party', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='government.Party')),
            ],
            options={
                'unique_together': {('election_event', 'party')},
            },
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='dem_primary_type',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='early_vote_close',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='early_vote_start',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='gop_primary_type',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='label',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='online_registration_deadline',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='poll_closing_time',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='registration_deadline',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='vote_by_mail_application_deadline',
        ),
        migrations.RemoveField(
            model_name='electionevent',
            name='vote_by_mail_ballot_deadline',
        ),
        migrations.AddField(
            model_name='election',
            name='election_ballot',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='elections', to='election.ElectionBallot'),
            preserve_default=False,
        ),
    ]
