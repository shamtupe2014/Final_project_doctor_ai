from django import forms
from .models import GenomeUpload
from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms
from .models import GenomeUpload


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    middle_name = forms.CharField(required=False)
    mobile_number = forms.CharField()
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'middle_name', 'last_name', 'email', 'mobile_number', 'date_of_birth', 'password']


class GenomeForm(forms.ModelForm):
    class Meta:
        model = GenomeUpload
        fields = ['genome_file']