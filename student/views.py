from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def list(request):
    context = {}
    return render(request, 'student/list.html', context)

def student_form(request):
    context = {}
    return render(request, 'student/form.html', context)

def student_delete(request):
    context = {}
    return render(request, 'student/list.html', context)