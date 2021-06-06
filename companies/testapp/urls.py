from django.urls import path
from testapp import views


urlpatterns=[
    path('',views.Company_list.as_view()),
    path('detail/<pk>',views.Company_details.as_view(),name='detail'),
    path('create/',views.Companay_create.as_view()),
    path('update/<pk>',views.Companay_update.as_view()),
    path('delete/<pk>',views.Company_delete.as_view()),
    path('del/<pk>',views.Company_delete.as_view()),
]