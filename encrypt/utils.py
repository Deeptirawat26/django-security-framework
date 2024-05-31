import os
from django.conf import settings

def handle_uploaded_file(uploaded_file):
    # file upload location
    save_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
    
    with open(save_path, 'wb') as destination:
        for chunk in uploaded_file.chunks():
            destination.write(chunk)
    
    return save_path
