from django import forms
from .models import FeedBack


class FeedbackCreate(forms.ModelForm):

    class Meta:
        model = FeedBack
        fields = ['name', 'email', 'subject', 'message']
