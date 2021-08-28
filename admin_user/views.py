from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.success(request,("invalid credentials"))
            return redirect('admin-login')
    else:
        return render(request,'authenticate/admin_login.html',{})

def admin_logout(request):
    logout(request)
    messages.success(request,("You Were Logged Out!!"))
    return redirect('admin-login')