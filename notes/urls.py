from django.contrib import admin
from django.urls import path
from document.views import editor, delete_document , generate_text
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('generate_text/', generate_text, name='generate_text'),  
]
