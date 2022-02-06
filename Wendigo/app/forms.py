from email.policy import default
from django import forms
from numpy import place

class CreateQuery(forms.Form):
    query = forms.CharField(label="Query",max_length=100) # ADD A DEFAULT OPTION