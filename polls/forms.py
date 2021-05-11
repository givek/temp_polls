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


class ChoiceModelForm(forms.ModelForm):
    choice_text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'choice-input form-input',
        'placeholder': 'option',
    }))

    class Meta:
        model = Choice
        fields = ['choice_text']


ChoiceInlineFormSet = forms.inlineformset_factory(
    Poll,
    Choice,
    form = ChoiceModelForm,
    fields = ('choice_text', ),
    extra = 0,
    min_num = 2,
    can_delete = False,
)
