from django import forms
from django.contrib.auth.models import User

from user.models import  Profile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('location',)

# class RegistrationForm(forms.ModelForm):
#     class Meta:
#         password= forms.CharField(widget=forms.PasswordInput())
#         model = Registration
#
#         fields = ('username', 'email', 'password')
#
#     def clean_username(self):
#             try:
#                 user = User.objects.get(username__iexact=self.cleaned_data['username'])
#             except User.DoesNotExist:
#                 return self.cleaned_data['username']
#             raise forms.ValidationError(_("The username already exists. Please try another one."))
#
#     def clean_passowrd(self):
#         if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
#             if self.cleaned_data['password1'] != self.cleaned_data['password2']:
#                 raise forms.ValidationError(_("The two password fields did not match."))
#         return self.cleaned_data
#
#
#
# class ProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ('bio', 'location', 'birthday')