from django import forms

from polls.models import Poll, Choice


class PollModelForm(forms.ModelForm):
    question = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'question-input form-input',
        'placeholder': 'maximum 175 words.',
    }))
    duration = forms.DateTimeField(widget=forms.DateInput(attrs={
        'class': 'duration-input form-input',
        'type': 'date',
    }))

    class Meta:
        model = Poll
        fields = '__all__'