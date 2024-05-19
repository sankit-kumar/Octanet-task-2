from django import forms
from tudoapp.models import tudoapp
class regi(forms.ModelForm):
    class Meta:
        model=tudoapp
        fields='__all__'
        labels={'name':'Enter the name :','email':'Enter the email id :','mob':'Enter the phone no :','password':'Enter the password :'}
        error_messages={'name':{'required':'enter your name'}}
        widgets={'password':forms.PasswordInput(attrs={'class':'','placeholder':'Enter your password '}),'name':forms.TextInput(attrs={'class':'','placeholder':'Enter your Name'}),'email':forms.EmailInput(attrs={'class':'','placeholder':'Enter your Email Id '}),'mob':forms.TextInput(attrs={'class':'','placeholder':'Enter your Phone Number '})}
