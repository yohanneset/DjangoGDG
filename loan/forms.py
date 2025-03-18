from django import forms
from .models import Loan

class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('name', 'amount', 'date', 'reason')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
