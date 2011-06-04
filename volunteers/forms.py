from django import forms
from models import Call

class CallForm(forms.ModelForm):

    where = forms.CharField(widget=forms.widgets.HiddenInput)

    class Meta:
        model = Call