from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def open_signup(request):
    return render(request, "signup.html")

def open_signin(request):
    return render(request, "signin.html")

def signup(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        password = request.POST.get("password")
        address = request.POST.get("address")
        return HttpResponse(f"Username: {username}, Password: {password}, Email: {email}, Mobile: {mobile}, Address: {address}")
    else:
        return HttpResponse("Invalid Response")
        
