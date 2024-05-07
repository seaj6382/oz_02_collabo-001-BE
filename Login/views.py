from django.shortcuts import render
from django.contrib. auth import authenticate, login, logout
from django.shortcuts import redirect
from .models import user
# Create your views here.


def login_view(request):
    if request.method == "POST":
        username =request.POST["username"]
        password =request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            print("인증성공")
            login(request, user)
        else:
            print("인증실패")

    return render(request, "users/login.html")

def logout_view(request) :
    logout(request)
    return redirect("Login:login")


def signup_view(request) :

    if request.method == "POST":
        print(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        user.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        return redirect("Login:login")

    return render(request, "users/signup.html")