from django import forms
from .models import EncryptedFile

class EncryptedFileUploadForm(forms.ModelForm): 
    class Meta:
        model = EncryptedFile 
        fields = ('file_name','file','username',) 
