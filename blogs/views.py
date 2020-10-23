from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.


def hello(request):
    # query data from model
    data = Post.objects.all()
    return render(request, 'landingpage.html', {'posts': data})

def  index (request):
    data = Post.objects.all()
    return render (request,'index.html',{'posts': data})

def page1(request):
        return render(request, 'page1.html')

def addCustomers(request):
    
    if request.method=="POST":
        print("saved")
        name = request.POST['name']
        line = request.POST['line']
        phone = request.POST['phone']
        address = request.POST['address']

        addCustomer = Post(name=name, line=line, phone=phone, address=address)
        addCustomer.save()
        return render(request, 'result.html')



def page2 (request):
    return render(request,'landingpage.html')



def createForm(request):
    return render(request, 'form.html')


def addForm(request):
    name = request.POST['name']
    line = request.POST['line']
    phone = request.POST['phone']
    address = request.POST['address']

    return render(request, 'result.html',
                  {'name': name,
                   'line': line, 'phone': phone, 'address': address})

def createPackage(request):
    return render(request, 'addpackage.html')

# def addCustomers(request):
    
#     if request.method=="POST":
#         print("saved")
#         name = request.POST['name']
#         line = request.POST['line']
#         phone = request.POST['phone']
#         address = request.POST['address']

#         addCustomer = Post(name=name, line=line, phone=phone, address=address)
#         addCustomer.save()
#         return render(request, 'result.html')


def addUser(request):
    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    email = request.POST['email']

    if password == repassword:
        if User.objects.filter(username=username).exists():
            messages.info(request, 'User is already used')
            return redirect('/createForm')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Email is already used')
            return redirect('/createForm')
        else:
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
        user.save()
        return redirect('/')
    else:
        messages.info(request, 'User is already used')
        return redirect('/createForm')


def loginForm(request):
    return render(request, 'login.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return redirect('/')
    else:
        messages.info(request, 'Username or Password incorrect')
        return redirect('/loginForm')


def logout(request):
    auth.logout(request)
    return redirect('/')
