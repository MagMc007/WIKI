from django.db import models
from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.Textarea()

