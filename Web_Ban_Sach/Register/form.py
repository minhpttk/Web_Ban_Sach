from django import forms
 
class registerForm(forms.Form):
    user_name=forms.CharField()
    email = forms.EmailField()
    password = forms.CharField( widget=forms.PasswordInput)

