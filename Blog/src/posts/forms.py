from cProfile import label
from collections import OrderedDict
from logging import PlaceHolder
from allauth import *
from allauth.account.forms import LoginForm, PasswordField, set_form_field_order
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post, Comment



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('__all__')
        labels = {
            'title': _('Titulo del Post'),
            'content': _('Contenido'),
            'thumbnail': _('Imagen'),
            'author': _('Autor')
        }

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

class MyLoginForm(LoginForm):
    password = PasswordField(label=("Contraseña"), autocomplete="current-password")
    remember = forms.BooleanField(label=("Recuerdame"), required=False)

    error_messages = {
        "account_inactive": _("Esta cuenta está inactiva"),
        "email_password_mismatch": _(
            "El email y/o la contraseña especificada no son correctas"
        ),
        "username_password_mismatch": _(
            "El usuario y/o contraseña no son correctas"
        ),
    }
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super(LoginForm, self).__init__(*args, **kwargs)
        login_widget = forms.TextInput(
            attrs={"placeholder": _("Usuario"), "autocomplete": "username"}
        )
        login_field = forms.CharField(
            label='Usuario',
            widget=login_widget
        )
        self.fields["login"] = login_field
        set_form_field_order(self, ["login", "password", "remember"])
        