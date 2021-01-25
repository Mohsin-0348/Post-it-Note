from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
from django.apps import apps
# from .models import *
from .forms import *


def home_view(request):
    obj_list = Users.objects.all()
    my_form = LoginForm()
    for obj in obj_list:
        if obj.is_active:
            x = make_password(obj.password)
            print(obj.user_name, x)
            return redirect('../' + obj.user_name + '/' + obj.password)
    else:
        return render(request, 'st_home.html')


def home(request, foo, goo):
    obj = Users.objects.get(user_name=foo, password=goo)
    model = apps.get_model('note', foo)
    obj_list = model.objects.all()
    context = {
        'user': obj,
        'object_list': obj_list
    }
    return render(request, 'note/list.html', context)


def note_detail(request, foo, goo, id):
    object = Users.objects.get(user_name=foo, password=goo)
    model = apps.get_model('note', foo)
    obj = get_object_or_404(model, id=id)
    context = {
        'object': obj,
        'user': object
    }
    return render(request, 'note/detail.html', context)


def note_create(request, foo, goo):
    obj = Users.objects.get(user_name=foo, password=goo)
    model = apps.get_model('note', foo)
    obj_list = model.objects.all()
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('description'):
            post = model()
            post.title = request.POST.get('title')
            post.description = request.POST.get('description')
            post.save()

            return redirect('../')
        else:
            return redirect('../')
    else:
        return render(request, 'note/create.html', {'user': obj})


def note_update(request, foo, goo, id):
    object = Users.objects.get(user_name=foo, password=goo)
    model = apps.get_model('note', foo)
    item = model.objects.get(id=id)
    my_form = NoteForm(instance=item)
    if request.method == 'POST':
        my_form = NoteForm(request.POST, instance=item)
        if my_form.is_valid():
            my_form.save()
            return redirect('../'+str(item.id))
    context = {
        'form': my_form,
        'user': object
    }

    # messages.success(request, 'Item has been edited')

    return render(request, 'note/update.html', context)


def note_delete(request, foo, goo, id):
    object = Users.objects.get(user_name=foo, password=goo)
    model = apps.get_model('note', foo)
    obj = get_object_or_404(model, id=id)
    if request.method == "POST":
        obj.delete()
    context = {
        'object': obj,
        'user': object
    }
    return render(request, 'note/delete.html', context)


def logout(request, foo, goo):
    obj = Users.objects.get(user_name=foo, password=goo)
    obj.is_active = False
    obj.save()
    return redirect('../')


def user_id(request, foo, goo):
    obj = Users.objects.get(user_name=foo, password=goo)

    context = {
        'user': obj
    }
    return render(request, 'user_id.html', context)


def signup(request):
    obj_list = Users.objects.all()
    my_form = SingupForm()
    if request.method == 'POST':
        my_form = SingupForm(request.POST)
        if my_form.is_valid():
            user = my_form.cleaned_data.get("user_name")
            for item in obj_list:
                if user != item.user_name:
                    my_form.save()
                    print(user)
                else:
                    print("message X", user)
            return redirect('signup')
    context = {
        'form': my_form
    }

    return render(request, 'signup.html', context)


def login(request):
    obj_list = Users.objects.all()
    my_form = LoginForm()
    for obj in obj_list:
        if obj.is_active:
            print(obj.user_name)
            return redirect('../'+obj.user_name+'/'+obj.password)
        else:
            if request.method == 'POST':
                my_form = LoginForm(request.POST)
                if my_form.is_valid():
                    user = my_form.cleaned_data.get("user_name")
                    passwd = my_form.cleaned_data.get("password")
                    for item in obj_list:
                        if user == item.user_name and passwd == item.password:
                            item.is_active = True
                            item.save()
                            print(user, passwd)
                            return redirect('../'+item.user_name+'/'+item.password)
                    else:
                        print("message X", user)
                        messages.success(request, 'User-name or Password does not match')

                        return redirect('login')

    context = {
        'form': my_form,
        'object': obj_list,

    }

    return render(request, 'login.html', context)
