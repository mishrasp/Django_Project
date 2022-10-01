from django.urls import path
from . import views

urlpatterns = [
    path('message',views.message,name="message"),
     path('login',views.login,name="login"),
     path('',views.register,name="register"),
     path('add',views.add,name="add"),
     path('get',views.getall,name="get"),
     path('delete',views.delete,name="delete"),
     path('update',views.update,name="update"),

]