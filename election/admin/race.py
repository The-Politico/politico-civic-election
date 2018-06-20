from django import forms
from django.contrib import admin

from election.models import ElectionCycle


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        if hasattr(obj, 'name'):
            return obj.name
        elif hasattr(obj, 'date'):
            return obj.date
        else:
            return obj.label


class RaceAdminForm(forms.ModelForm):
    cycle = CustomModelChoiceField(queryset=ElectionCycle.objects.all())


class RaceAdmin(admin.ModelAdmin):
    form = RaceAdminForm
    list_display = ('get_office', 'get_cycle', 'special')
    autocomplete_fields = ['office']
    search_fields = ['office__label', 'cycle__name', 'label']
    ordering = ('office__label', 'cycle__name')

    def get_office(self, obj):
        return obj.office.label

    def get_cycle(self, obj):
        return obj.cycle.name

    get_office.short_description = 'Office'
    get_cycle.short_description = 'Cycle'
