from django import forms

class NameAgeSalaryForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=1)
    salary = forms.DecimalField(min_value=0.01, max_digits=10, decimal_places=2)
