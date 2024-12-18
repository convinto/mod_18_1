from django.shortcuts import render
from django.views.generic import TemplateView

class NewClass(TemplateView):
    template_name = 'class_template.html'

def new_func(request):
    return render(request, 'func_template.html')