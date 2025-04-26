from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, GenomeForm
from .models import GenomeUpload, Profile
from .ml_model import predict_disease
from .forms import CustomUserCreationForm


def homepage(request):
    return render(request, 'homepage.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            return redirect('login')  # Redirect to login page after successful registration
        else:
            # If form is invalid, print the errors and send back the form
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'homepage.html')

@login_required
def dashboard(request):
    prediction = None
    if request.method == 'POST':
        form = GenomeForm(request.POST, request.FILES)
        symptoms = request.POST.getlist('symptoms')
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.symptoms = ','.join(symptoms)
            instance.save()

            # Predict disease using ML model
            prediction = predict_disease(instance.genome_file.path, symptoms)

            return render(request, 'result.html', {
                'prediction': prediction,
                'file': instance.genome_file.name,
                'symptoms': symptoms
            })
    else:
        form = GenomeForm()

    return render(request, 'main.html', {'form': form, 'prediction': prediction})

@login_required
def result(request):
    return render(request, 'result.html')

def logout_view(request):
    logout(request)
    return redirect('login')