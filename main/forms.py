import re
from django import forms

class CreateFeedbackForm(forms.Form):

    subject_letter = forms.CharField()
    body_letter = forms.CharField()