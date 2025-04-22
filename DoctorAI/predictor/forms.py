from django import forms
from .models import GenomeUpload

class GenomeForm(forms.ModelForm):
    class Meta:
        model = GenomeUpload
        fields = ['genome_file']