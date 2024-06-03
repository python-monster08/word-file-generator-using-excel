from django.urls import path
from .views import upload_file_view, success_view, generate_questions_document, view_generate_document

urlpatterns = [
    path('upload/', upload_file_view, name='upload_file_view'),
    # other paths
    path('', success_view, name='success_view'),
    path('generate-doc/', generate_questions_document, name='generate_doc'),
    path('view-generate-doc/', view_generate_document, name='view_generate_doc'),
]
