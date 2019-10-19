from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import base64

from social_app.models import User

# Create your views here.
def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            user = None
            try:
                user = User.objects.get(pk=uname)
            finally:
                print(pwd)
                if user and user.password == base64.b64encode(pwd.encode()).decode():
                    del user.password
                    return render(request, 'home.html', {'user': user})
                return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        if uname and pwd:
            try:
                user = User(username = uname, password= base64.b64encode(pwd.encode()).decode())
                user.save()
                return render(request, 'signup.html', {'success': 'User registered successfully'})
            except Exception as e:
                print(e)
                return render(request, 'signup.html', {'error': 'Username already exist'})
        return render(request, 'signup.html', {'error': 'Fill all details properly'})
    return render(request, 'signup.html')

@login_required
def home(request):
    return render(request, 'home.html')