from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, RepairRequestForm
from .models import RepairRequest


# Create your views here.

def home_page_view(request):
    return render(request, 'layout.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get['username']
            password = form.cleaned_data.get['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_view(request, user)
                return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'registration/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def create_repair_request_view(request):
    if request.method == 'POST':
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = RepairRequestForm()

    return render(request, 'repair_request.html', {'form': form})

@login_required
def repair_request_list_view(request):
    repair_request = RepairRequest.objects.all()
    return render(request, 'repair_request_list.html', {'repair_request': repair_request})
