from django import forms
from .models import Book

class BookModelForm(forms.ModelForm):
    model=Book
    fields='__all__'

