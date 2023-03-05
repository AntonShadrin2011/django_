from django import forms
from .models import *


class CiteFrom(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Cite
        fields = ('name',)