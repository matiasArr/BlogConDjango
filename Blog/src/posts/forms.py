from allauth.account.forms import PasswordField
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 4
            }),
        }
        labels = {
            'content': _(''),
        }


       

class LoginForm(forms.ModelForm):
    password = PasswordField(label=("Password"), autocomplete="current-password")
    remember = forms.BooleanField(label=("Remember Me"), required=False)

    error_messages = {
        "account_inactive": ("This account is currently inactive."),
        "email_password_mismatch": (
            "The e-mail address and/or password you specified are not correct."
        ),
        "username_password_mismatch": (
            "The username and/or password no son correctas"
        ),
    }