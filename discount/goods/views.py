from django.http import HttpResponse
from django.shortcuts import render

from .models import Products, Register


def index(request):
    products = Products.objects.all()
    return render(request, "goods/index.html", {"products": products})


def register(request):
    return render(request, "goods/register.html")


def product(request):
    products = Products.objects.all()
    return render(request, "goods/product.html", {"products": products})


def addUser(request):
    if request.POST:
        try:
            loginUser = request.POST.get("login")
            password = request.POST.get("password")
            email = request.POST.get("email")
            response = f"Привет {loginUser}{password}{email}"
            dataBD = Register.objects.get_or_create(name=loginUser, password=password, email=email)
            # dataBD.save()
        except ValueError:
            with open("loger.txt", "a") as loger:
                loger.write("Нет данных")
    else:
        response = "не работает"
    return HttpResponse(response)
    # return render(response, "goods/register.html")


def user_register(request):
    user_reg = Register.objects.all()
    return HttpResponse(user_reg)


def add_products(request):
    products = Products.objects.all()
    return HttpResponse(products)
