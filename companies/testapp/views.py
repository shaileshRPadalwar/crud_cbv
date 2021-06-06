from django.shortcuts import render
from .models import Company
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.urls import reverse_lazy



# Create your views here.


#list view
class Company_list(ListView):
    model=Company

class Company_details(DetailView):
    model=Company

class Companay_create(CreateView):
    model=Company
    fields=('name','location','ceo')


class Companay_update(UpdateView):
    model=Company
    fields=('name','ceo')

class Company_delete(DeleteView):
    model=Company
    success_url='/'
    