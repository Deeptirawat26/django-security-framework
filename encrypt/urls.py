from django.urls import path
from . import views
from .views import view_file

urlpatterns = [
     path('view/<int:file_id>/', view_file, name='view_file'), 
]
