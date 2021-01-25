from django import forms
from .models import *


class NoteForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Title..."}))
    description = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                "class": "new-class-name two",
                "rows": 8,
                "cols": 40,
            }
        )
    )

    class Meta:
        model = Note
        fields = [
            'title',
            'description'
        ]


class SingupForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={"placeholder": "First name..."}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(attrs={"placeholder": "Last name..."}))
    user_name = forms.CharField(label="User Name", widget=forms.TextInput(attrs={"placeholder": "User name..."}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "example@gmail.com"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password..."}))
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Rewrite password..."}))

    class Meta:
        model = Users
        fields = [
            'first_name',
            'last_name',
            'user_name',
            'email',
            'password',
            're_password'
        ]

    def clean(self):
        cleaned_data = super(SingupForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("re_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password and confirm_password does not match"
            )


class LoginForm(forms.ModelForm):
    user_name = forms.CharField(label="User-name", widget=forms.TextInput(attrs={"placeholder": "User name..."}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Password..."}))

    class Meta:
        model = Users
        fields = [
            'user_name',
            'password'
        ]
