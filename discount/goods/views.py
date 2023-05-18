from django.http import HttpResponse
from django.shortcuts import render
from .models import Register, Products


# Create your views here.
def index(request):
    return render(request, 'good/index.html')

def register(request):
    return render(request, 'good/register.html')

def addUser(request):
    if request.POST:
        try:
            loginUser = request.POST.get("login")
            password = request.POST.get("password")
            email = request.POST.get("email")
            response = f'Привет {loginUser}{password}{email}'
            dataBD = Register.objects.get_or_create(name=loginUser, password=password, email=email)
            # dataBD.save()
        except ValueError:
            print("Нет данных")
    else:
        response = 'не работает'
    return HttpResponse(response)
    # return render(response, 'good/register.html')
def user_register(request):
    user_reg = Register.objects.all()
    return HttpResponse(user_reg)

def add_products(request):
    products = Products.objects.all()
    return HttpResponse(products)