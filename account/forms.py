from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import User, History_Book, Rank_Book

class SignUpForm(UserCreationForm):
    ROLE_CHOICES = User.ROLE_CHOICES  # Assuming you have ROLE_CHOICES in your User model
    role = forms.ChoiceField(choices=ROLE_CHOICES, label='Role', required=True)
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')  # Include 'role' in the fields

class History_Book_Form(forms.ModelForm):
    class Meta:
        model = History_Book
        fields = ['profile']

class Rank_Book_Form(forms.ModelForm):
    class Meta:
        model = Rank_Book
        fields = ['profile']
