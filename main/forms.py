from django import forms


class TimeForm(forms.Form):
    hour=forms.IntegerField(min_value=0,required=False)
    minute=forms.IntegerField(min_value=0,required=False)
    condition=forms.CharField(max_length=50,required=False)
