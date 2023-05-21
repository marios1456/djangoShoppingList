#from django.conf.global_settings import AUTH_USER_MODEL
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import ShoppingItem
#from django.conf import settings
from django.contrib.auth.models import User

# Create your views here.


def mylist(request):
    if not request.user.is_authenticated:
        return redirect(loginForm)

    if request.method == "POST":
        print("Received data: ", request.POST["itemName"], "from user: ", request.user)#
        ShoppingItem.objects.create(name=request.POST["itemName"], user= request.user)

    all_items = ShoppingItem.objects.filter(user=request.user)
    return render(request, "shoping_list.html", {'all_items': all_items})


def delete_item(request, id):
    if request.method == "DELETE":
        print("Received data: ", request, id)
        ShoppingItem.objects.filter(id=id).delete()

    if request.method == "PUT":
        print("Received data: ", request, id)
        item = ShoppingItem.objects.get(id=id)
        item.done = not item.done
        item.save()

    return redirect(mylist)


def loginForm(request):
    if request.user.is_authenticated:
        logout(request)
    return render(request, "loginForm.html", {'messages': ""})


def loginformcheck(request):
    print(request)
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            print("user ok")
            login(request, user)
            return redirect(mylist)
        else:
            print("User not ok")
            message = "User not found"
            return render(request, "loginForm.html", {'messages': message, "username": username, "password": password})


