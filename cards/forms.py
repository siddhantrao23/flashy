from django import forms

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
