from django.shortcuts import render,get_object_or_404
from testapp.models import Book
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse

from django.views.generic.edit import CreateView, UpdateView


# Create your views here.

# Hello world application by using CBV
class Book(View):
    def get(self,request):
        return HttpResponse('This is from class Based Views')

#template based application by using CBV
class TemplateCBV(TemplateView):
    template_name='base1.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='shailesh'
        context['age']='21'
        return context

#ListView
class Booklist(ListView):
    model=Book

#DetailView
class DetailView_Book(DetailView):
    model=Book

#createView
class CreateView_Book(CreateView):
    model=Book
    fields=['title','author','pages','price']
    success_url = '/thanks/'



    

