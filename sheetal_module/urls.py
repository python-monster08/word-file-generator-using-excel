from django.urls import path
from .views import display_questions, question_view, question_detail, add_questions, submit_question

urlpatterns = [
    path('questions/', display_questions, name='display-questions'),
    # path('questions/<int:question_no>/', question_view, name='question-detail'),
    path('questions/<int:question_no>/', question_detail, name='question-detail'),
    path('add_questions/', add_questions, name='add_questions'),# URL to display the form
    path('submit-question/', submit_question, name='submit_question'),  # URL for form submission
]
