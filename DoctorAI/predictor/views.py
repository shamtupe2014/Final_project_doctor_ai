from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import GenomeForm
from .models import GenomeUpload
from .ml_model import predict_disease


def homepage(request):
    return render(request, 'homepage.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    if request.method == 'POST':
        form = GenomeForm(request.POST, request.FILES)
        symptoms = request.POST.getlist('symptoms')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.symptoms = ','.join(symptoms)
            instance.save()
            prediction = predict_disease(instance.genome_file.path, symptoms)
            return render(request, 'result.html', {'prediction': prediction})
    else:
        form = GenomeForm()
    return render(request, 'main.html', {'form': form})


def result(request):
    return render(request, 'result.html')
