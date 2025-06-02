from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Lesson

def home(request):
    courses = Course.objects.all()
    return render(request, 'main/home.html', {'courses': courses})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})


def course_list(request):
    courses = Course.objects.all()
    return render(request, 'main/course_list.html', {'courses': courses})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lessons = Lesson.objects.filter(course=course).order_by('order')
    return render(request, 'main/course_detail.html', {'course': course, 'lessons': lessons})

def about(request):
    return render(request, 'main/about.html')
