from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Pack
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth


# Create your views here.

# homepage


def hello(request):
    return render(request, 'landingpage.html')


def index(request, pk):
    # query data from model Post
    print(Post.objects.filter(user_id=pk).query)
    data = Post.objects.filter(user_id=pk)
    return render(request, 'index.html', {'posts': data})


def index2(request):
    # query data from model Pack
    data = Pack.objects.all()
    return render(request, 'index2.html', {'packs': data})

# add customer


def page1(request):
    return render(request, 'page1.html')


def addCustomers(request, pk):

    if request.method == "POST":
        print("saved")
        name = request.POST['name']
        line = request.POST['line']
        phone = request.POST['phone']
        address = request.POST['address']
        status = request.POST.get('status')
        size = request.POST.get('size')
        types = request.POST.get('types')
        packname = request.POST['packname']
        print(status)
        id = pk
        print(pk)
        addCustomer = Post(name=name, line=line,
                           phone=phone, address=address, status=status, size=size, types=types, packname=packname, user_id_id=id)
        addCustomer.save()

        return render(request, 'result.html')

# delete


# def DeleteCus(request, pk):
#     obj = get_object_or_404(Post, id=pk)
#     if request.method == "POST":
#         obj.delete()
#         return render(request, 'result.html')
#     context = {
#         "object": obj
#     }
#     return render(request, 'result.html')


def page2(request):
    return render(request, 'landingpage.html')


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

# addpackage


def createPackage(request):
    return render(request, 'addpackage.html')


def addPackage(request):

    if request.method == "POST":
        print("saved")
        trackingno = request.POST['trackingno']
        size = request.POST['size']
        phone = request.POST['phone']
        address = request.POST['address']

        addPackage = Pack(trackingno=trackingno, size=size,
                          phone=phone, address=address)
        addPackage.save()
        return render(request, 'result.html')


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
