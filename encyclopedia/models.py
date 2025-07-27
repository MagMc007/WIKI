from django.db import models
from django import forms


class NewPageForm(forms.Form):
    title = forms.CharField(max_length=100)
    Content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Enter content here ...",
        "rows": 10, "cols": 50
    }))
