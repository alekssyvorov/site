from django.http import HttpResponse
from django.shortcuts import render
from .models import Register

# Create your views here.
def index(request):
    return HttpResponse("<h2>Привет мир</h2>")

def register(request):
    return render(request, 'good/register.html')

def addUser(request):
    print(request)
    if request.POST:
        try:
            loginUser = request.POST.get("login")
            password = request.POST.get("password")
            email = request.POST.get("email")
            response = f'Привет {loginUser}{password}{email}'
            print(response)
            dataBD = Register(name=loginUser, password=password, email=email)
            dataBD.save()
        except:
            print("Нет данных")
    else:
        response = 'не работает'
    return HttpResponse(response)
    # return render(request, 'good/register.html')
def user_register(request):
    user_reg = Register.objects.all()
    return HttpResponse(user_reg)