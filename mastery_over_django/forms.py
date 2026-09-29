from django import forms

from mastery_over_django.models import Mastery


class MasteryForm(forms.ModelForm):
    class Meta:
        model = Mastery
        fields = ['mastery_name','mastery_description']