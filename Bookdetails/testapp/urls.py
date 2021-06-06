from django.urls import path
from testapp import views
from testapp.models import Book


urlpatterns=[
    path('',views.Book.as_view()),
    path('template/',views.TemplateCBV.as_view()),
    path('list/',views.Booklist.as_view(model=Book)),
    path('detail/<pk>',views.DetailView.as_view(model=Book)),
    path('create/',views.CreateView.as_view(model=Book)),
]







