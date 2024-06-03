from django.shortcuts import redirect, render, get_object_or_404
from question_module.models import Question, DefficultyLevel
from django.http import Http404
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from PIL import Image
import io
from django.core.files.images import ImageFile
from django.utils.html import mark_safe, escape
# Create your views here.


def display_questions(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    return render(request, 'sheetal_module/questions_display.html', {'questions': questions})


def question_view(request, question_no):
    question = get_object_or_404(Question, question_no=question_no)
    return render(request, 'sheetal_module/questions_display.html', {'question': question})




def question_detail(request, question_no):
    question = get_object_or_404(Question, question_no=question_no)
    all_questions = Question.objects.all().order_by('question_no')
    try:
        previous_question = Question.objects.filter(question_no__lt=question.question_no).order_by('-question_no').first()
        next_question = Question.objects.filter(question_no__gt=question.question_no).order_by('question_no').first()
    except Question.DoesNotExist:
        previous_question = None
        next_question = None

    context = {
        'question': question,
        'previous_question_no': previous_question.question_no if previous_question else None,
        'next_question_no': next_question.question_no if next_question else None,
        'all_questions': all_questions,
    }
    
    return render(request, 'sheetal_module/questions_display.html', context)


def add_questions(request):
    difficulties = DefficultyLevel.objects.all()
    return render(request, 'sheetal_module/add_question.html', {"difficulties":difficulties})

    


def submit_question(request):
    if request.method == 'POST':
        # Extract data from form
        question_text = request.POST.get('question_text')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')
        option_d = request.POST.get('option_d')
        correct_answer_option = request.POST.get('correct_answer_option')
        correct_answer_description = request.POST.get('correct_answer_description')
        topic = request.POST.get('topic')
        area = request.POST.get('area')
        level_of_difficulty_id = request.POST.get('level_of_defficulty')
        level_of_defficulty = DefficultyLevel.objects.get(id=level_of_difficulty_id)  # Ensure name matches
        # Define the FileSystemStorage instance
        fs = FileSystemStorage()

        image = request.FILES.get('image')
        if image:
            # Convert image to RGB if it's RGBA (to remove alpha channel)
            pil_image = Image.open(image)
            if pil_image.mode == 'RGBA':
                pil_image = pil_image.convert('RGB')
            
            # Save the converted image to a new file-like object
            new_image_io = io.BytesIO()
            pil_image.save(new_image_io, format='JPEG')  # Save as JPEG

            # Create a Django-friendly File object
            new_image_io.seek(0)  # Important: move back to the start of the BytesIO object
            new_image_file = ImageFile(new_image_io, name=image.name.replace('.png', '.jpg'))
            uploaded_file_url = fs.save(new_image_file.name, new_image_file)
        else:
            uploaded_file_url = None
        # Creating and saving the new question instance
        question = Question(
            question_no = Question.objects.all().count() + 1,
            question_text=question_text,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c,
            option_d=option_d,
            correct_answer_option=correct_answer_option,
            # image=image,
            image=uploaded_file_url,
            correct_answer_description=correct_answer_description,
            topic=topic,
            area=area,
            level_of_defficulty=level_of_defficulty
        )
        question.save()

        return redirect('success_view')  # Ensure you have this URL configured in urls.py
    else:
        return render(request, 'sheetal_module/add_question.html')