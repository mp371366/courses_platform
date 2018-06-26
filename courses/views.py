from django.shortcuts import render, get_object_or_404

from courses.models import *

def home(request):
    context = {
        'courses': Course.objects.all(),
    }
    
    return render(request, 'courses/home.html', context)

def course(request, course_id):
    context = {
        'course': get_object_or_404(Course, id=course_id),
    }

    return render(request, 'courses/course.html', context)
