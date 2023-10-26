from django import forms
from .models import *


class userform(forms.ModelForm):

    class Meta:
        model = UserDetail
        fields = ('first_name','last_name', 'email', 'mobno')

