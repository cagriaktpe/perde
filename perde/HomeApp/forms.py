from django import forms
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

'''class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'date_joined']  # Profil alanlarını burada belirtin
'''
class UserProfileForm(forms.ModelForm):
    joined = forms.DateTimeField(disabled=True, required=False)
    email = forms.CharField(max_length=100, label='email', disabled=True)

    class Meta:
        model = UserProfile
        fields = ['ad', 'soyad', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.initial['ad'] = self.instance.user.first_name
            self.initial['soyad'] = self.instance.user.last_name
            self.initial['email'] = self.instance.user.email
            self.initial['joined'] = self.instance.user.date_joined

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    email = forms.EmailField(max_length=100, label='Email')
    password1 = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
    
            

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)