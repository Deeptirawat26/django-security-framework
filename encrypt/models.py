from django.db import models
from django.http import HttpResponse 

class EncryptedFile(models.Model):
    file_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='encrypted/') 
    username = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name

    def view(self):
        with open(self.file.path, 'rb') as file:
            response = HttpResponse(file.read(), content_type='application/octet-stream')
            response['Content-Disposition'] = f'inline; filename="{self.file_name}"'
            return response 
    

    