from django import forms
from cards.models import Set, Card

class LoginForm(forms.Form):
    username = forms.CharField(label='Name', max_length=100)
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput, max_length=100
    )

class SetForm(forms.Form):
    set_name = forms.CharField(label='Set Name', max_length=100)
    description = forms.CharField(
        label='Description', max_length=300, required=False
    )
    private = forms.BooleanField(label='Private', required=False)

class CardForm(forms.Form):
    question_text = forms.CharField(label='Question', max_length=300)
    answer_text = forms.CharField(label='Answer', max_length=300)

class DelSetForm(forms.Form):
    selected_set = forms.ModelChoiceField(
        queryset=Set.objects.all().order_by('set_name')
    )

class DelCardForm(forms.Form):
    selected_card = forms.ModelChoiceField(
        # TODO change query set dynamically
        queryset=Card.objects.all().order_by('question_text')
    )
