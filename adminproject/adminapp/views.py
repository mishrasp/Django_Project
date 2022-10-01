from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from adminapp.models import Book
from django.contrib import messages


# Create your views here.
def message(request):
    return render(request,"message.html")
def login(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=auth.authenticate(username=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("get")
    else:
        return render(request,"login.html")
def register(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        if(password==confirm_password):
            user=User.objects.create_user(username=email,password=password)
            user.save()
            return redirect("login")
    else:
        return render(request,"register.html")        

def add(request):
    if(request.method=='POST'):
        book_id=request.POST.get('book_id')
        book_name=request.POST.get('book_name')
        writer_name=request.POST.get('writer_name')
        book=Book(book_id=book_id,book_name=book_name,writer_name=writer_name)
        book.save()
        messages.info(request,"added Successfully")
        return redirect("get")
    else:
        return render(request,"add.html")
def getall(request):
    data=Book.objects.all()
    return render(request,"display.html",{'data':data})
def delete(request):
    if(request.method=='POST'):
        id=request.POST.get('id')
        d1=Book.objects.get(book_id=id)
        d1.delete()
        return render("get")
    else:
        return render(request,"delete.html")    
def update(request):
    if(request.method=='POST'):
        book_id=request.POST.get('book_id')
        book_name=request.POST.get('book_name')
        writer_name=request.POST.get('writer_name')
        u=Book.objects.get(book_id=book_id)
        u.book_name=book_name
        u.writer_name=writer_name
        u.save()
        return redirect("get")
    else:
        return render(request,"update.html")

