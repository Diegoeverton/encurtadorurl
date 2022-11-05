from django import forms
from .models import Links
class FormLInks(forms.ModelForm):
    class Meta:
        model = Links
        fields = "__all__"