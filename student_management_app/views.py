from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from student_management_app.EmailBackEnd import EmailBackend


def home(request):
    return render(request, "index.html")


def login_page(request):
    return render(request, "login.html")

def do_login(request):
    if request.method != "POST":
        return HttpResponse("Invalid request method")

    email = request.POST.get("email")
    password = request.POST.get("password")

    user = EmailBackend.authenticate(request, username=email, password=password)

    if user is None:
        messages.error(request, "Invalid login credentials")
        return redirect("login")

    login(request, user)

    if user.user_type == 1:
        return redirect("admin_home")
    elif user.user_type == 2:
        return redirect("staff_home")
    elif user.user_type == 3:
        return redirect("student_home")

    messages.error(request, "User role not recognized")
    return redirect("login")


def logout_user(request):
    logout(request)
    return redirect("login")

def get_user_details(request):
    if request.user.is_authenticated:
        return HttpResponse(f"User: {request.user.email} | Type: {request.user.user_type}")
    return HttpResponse("Please login first")