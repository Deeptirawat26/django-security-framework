from django.contrib import messages 
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseNotFound
from .forms import EncryptedFileUploadForm
from .models import EncryptedFile
from encrypted_files.base import EncryptedFile as EF 
from easyaudit.models import CRUDEvent
from django.contrib.contenttypes.models import ContentType

def upload_file(request):
    if request.method == 'POST':
        form = EncryptedFileUploadForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            file_name = form.cleaned_data['file_name']
            file = form.cleaned_data['file'] 
            username = form.cleaned_data['username'] 
            messages.success(request, 'File uploaded successfully.') 
            return redirect('dashboard')  
    else:
        form = EncryptedFileUploadForm() 
    
    return render(request, 'upload.html', {'form': form}) 


def view_file(request, file_id):
    encrypted_file = get_object_or_404(EncryptedFile, pk=file_id)
    
    if request.user.username != encrypted_file.username:
        
        CRUDEvent.objects.create(
            event_type=1, 
            object_id=str(encrypted_file.pk),
            content_type=ContentType.objects.get_for_model(encrypted_file),
            object_repr=str(encrypted_file),
            changed_fields=None,
            user=request.user,
        )
        return HttpResponseNotFound("You are not authorized to access this file")

    ef = EF(encrypted_file.file)  
    decrypted_content = ef.read()

    if encrypted_file.file.name.endswith('.pdf'):
        content_type = 'application/pdf'
    elif encrypted_file.file.name.endswith('.docx'):
        content_type = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    else:
        # Default 
        content_type = 'text/plain'
    
    CRUDEvent.objects.create(
        event_type=1,   
        object_id=str(encrypted_file.pk),
        content_type=ContentType.objects.get_for_model(encrypted_file),
        object_repr=str(encrypted_file),
        changed_fields=None,
        user=request.user,
    )

    return HttpResponse(decrypted_content, content_type=content_type)
