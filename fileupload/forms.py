from django import forms
from .models import UploadedFile
from multiupload.fields import MultiFileField

class FileUploadForm(forms.ModelForm):
    files = MultiFileField(min_num=1, max_num=5)

    class Meta:
        model = UploadedFile
        fields = ['name', 'files', 'file_type', 'tech_stack']
