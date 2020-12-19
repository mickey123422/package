from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Pack, profiles
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import get_user_model
from .forms import EditForm
from django.core.paginator import Paginator
# Create your views here.


# homepage


def hello(request):
    return render(request, 'landingpage.html')


def index(request, pk):
    # query data from model Post
    # print(Post.objects.filter(user_id=pk).query)
    data = Post.objects.filter(user_id=pk)
    datacount = Post.objects.filter(user_id=pk).count()
    count = data.count()
    print(count)
    return render(request, 'index.html', {'posts': data, 'count': count})


def index2(request):
    # query data from model Pack
    User = get_user_model()
    users = User.objects.all()
    count = users.all().count()
    user_profiles = profiles.objects.all()

    return render(request, 'index2.html', {'users': users, 'count': count, 'user_profiles': user_profiles})

# add customer


def page1(request):
    users = profiles.objects.all()
    return render(request, 'page1.html', {'users': users})


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
        sensorid = request.POST.get('sensorid')
        packname = request.POST['packname']
        adminadd = request.POST.get('adminadd')
        id = pk

        if adminadd == None:

            adminadd = pk
            print('role = user')

        else:
            size = request.POST.get('size')

            print('role = admin')
            print(status)
            print(pk)
            print(size)
            print(adminadd)
        addCustomer = Post(name=name, line=line,
                           phone=phone, address=address, status=status, size=size, types=types, packname=packname, user_id_id=adminadd, sensorid=sensorid)
        addCustomer.save()

        return render(request, 'result.html')

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


# deleteCustomer
def DeleteCus(request, pk):
    data = Post.objects.get(id=pk)

    if request.method == "POST":
        data.delete()
        return render(request, 'landingpage.html')
    return render(request, 'Delete.html', {'post': data})

# update


def EditCustomer(request, pk):
    data = Post.objects.get(id=pk)
    print(data)
    return render(request, 'edit.html', {'post': data})


def CreateEdit(request, pk):
    data = Post.objects.get(id=pk)
    form = EditForm(instance=data)
    print(data)
    if request.method == "POST":
        form = EditForm(request.POST, instance=data)
        if form.is_valid():
            form.save()

    return render(request, 'result.html', {'post': form})


# to landingpage
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


def addUser(request):

    username = request.POST['username']
    password = request.POST['password']
    repassword = request.POST['repassword']
    email = request.POST['email']

    storename = request.POST['storename']
    storephone = request.POST['storephone']
    storeaddress = request.POST['storeaddress']

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
            profile = profiles.objects.create(
                user_id=user,
                storename=storename,
                username=user,
                email=email,
                storephone=storephone,
                storeaddress=storeaddress,

            )

        return redirect('/')
    else:
        messages.info(request, 'User is already used')
        return redirect('/createForm')


# login
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


def Viewuser(request, pk):
    # query data from model Post
    # print(Post.objects.filter(user_id=pk).query)
    data = Post.objects.filter(user_id=pk)
    return render(request, 'Viewusercus.html', {'posts': data},)


def DeleteUser(request, pk):
    users = User.objects.get(id=pk)

    if request.method == "POST":
        users.delete()
        print(users)
        return render(request, 'landingpage.html')
    return render(request, 'DeleteUserPage.html', {'users': users})


def packdetail(request):
    return render(request, 'packdetail.html')
