from django.contrib import admin
from election.models import CandidateElection


class CandidateElectionInline(admin.StackedInline):
    model = CandidateElection
    extra = 0


class ElectionAdmin(admin.ModelAdmin):
    inlines = [
        CandidateElectionInline
    ]