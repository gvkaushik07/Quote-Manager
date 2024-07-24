from django import forms
from .models import Quote

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['author', 'text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 4}),
        }