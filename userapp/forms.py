from typing import Any
from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password1(self):
        cd = self.cleaned_data
        password1 = cd.get("password1")
        password2 = cd.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают!")
        
        return password1
        
    def save(self, commit = True):
        instance = self.cleaned_data
        user = super().save(commit=False)
        user.set_password(instance.get('password1'))
        if commit:
            user.save()
        return user