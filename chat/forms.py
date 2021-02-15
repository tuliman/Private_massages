from django import forms
from .models import Messages, Chats
from django.contrib.auth.models import User


class RegistrationUserForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email',)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают!')
        return cd['password2']


class SearchForm(forms.Form):
    search = forms.CharField(max_length=200, required=False, label='Search')

    def custom_search(self):
        cd = self.cleaned_data
        if len(User.objects.filter(username=cd['search'])) == 0:
            raise forms.ValidationError('Пользователя не существует')
        return cd['search']


class AuthUserForm(forms.Form):
    user_name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = '__all__'
        exclude = ('chat_id', 'author',)
