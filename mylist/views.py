from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import ShoppingItem

# Create your views here.


def mylist(request):
    # login(request, user)
    if request.method == "POST":
        print("Received data: ", request.POST["itemName"])#
        ShoppingItem.objects.create(name=request.POST["itemName"])

    all_items = ShoppingItem.objects.all()
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


