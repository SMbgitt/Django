from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from authap.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.urls import reverse


def login(request):
    title = 'вход'

    login_form = ShopUserLoginForm(data=request.POST)

    _next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            return HttpResponseRedirect(reverse('index'))
    context = {
        'title': title,
        'login_form': login_form,
        'next': _next,
    }

    return render(request, 'auth/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    title = 'регистриция'
    register_form = ShopUserRegisterForm()
    print(1)
    if request.method == "POST":
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        print(2)
        if register_form.is_valid():
            print(3)
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        print(4)
        register_form = ShopUserRegisterForm()
    context = {
        'title': title,
        'register_form': register_form,
    }

    return render(request, 'auth/register.html', context)

def edit(request):
    title = 'редактирование'

    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)

        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        edit_form = ShopUserEditForm(instance=request.user)

    context = {
        'title': title,
        'edit_form': edit_form,
    }

    return render(request, 'auth/edit.html', context)
