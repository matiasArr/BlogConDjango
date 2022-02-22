from dataclasses import field, fields
from tkinter import TRUE
from allauth import *
from allauth.account.forms import LoginForm, SignupForm , PasswordField, set_form_field_order
from django.utils.translation import gettext_lazy as _
from django import forms
from .models import Post, Comment
from ckeditor.widgets import CKEditorWidget



class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
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
    '''
     # NO SE MUESTRAS LOS MENSAJES QUE TIENE POR DEFECTO ALLAUTH
    '''
    
    password = PasswordField(
        label=_("password"), 
        required=True, 
        widget=forms.PasswordInput(
            attrs={
                "type": "password",
                "placeholder": _("contraseña")
            }
        )
    )
    
    remember = forms.BooleanField(label=_("Recuerdame"), required=False)
    
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
            attrs={"placeholder": _("usuario"), "autocomplete": "username"}
        )
        
        login_field = forms.CharField(
            label='',
            widget=login_widget
            
        )
        password_widget = forms.PasswordInput(
            attrs={"placeholder": _(""), "autocomplete": "password"}
        )
        password_field = PasswordField(
            label='',
            widget=password_widget
        )
        self.fields["login"] = login_field
        self.fields["password"] = password_field
        set_form_field_order(self, ["login", "password", "remember"])

    # modificar el form de signup para que se muestre de mejor manera
    
class MySignupForm(SignupForm):
    pass