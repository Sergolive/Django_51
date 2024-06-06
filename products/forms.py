from django import forms

class SearchForms(forms.Form):
    search = forms.CharField(max_length=256)