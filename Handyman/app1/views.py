from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import ClientSignUpForm, TechnicianSignUpForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ClientSignUpForm, TechnicianSignUpForm,UserForm
from .models import MaintenanceTechnician
def home(request):
    return render(request, 'home.html',)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('technician_list')
        else:
            messages.error(request, 'Identifiant ou mot de passe incorrect.')
    return render(request, 'login.html')

# Vue pour la déconnexion
def user_logout(request):
    logout(request)
    return redirect('home')  # Rediriger vers la page



def client_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        client_form = ClientSignUpForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            # Rediriger vers une page de confirmation
            return redirect('registration_success')
    else:
        user_form = UserForm()
        client_form = ClientSignUpForm()
    return render(request, 'client_register.html', {'user_form': user_form, 'client_form': client_form})

def technician_register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        technician_form = TechnicianSignUpForm(request.POST)
        if user_form.is_valid() and technician_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            technician = technician_form.save(commit=False)
            technician.user = user
            technician.save()
            # Rediriger vers une page de confirmation
            return redirect('registration_success')
    else:
        user_form = UserForm()
        technician_form = TechnicianSignUpForm()
    return render(request, 'technician_register.html', {'user_form': user_form, 'technician_form': technician_form})



def technician_list(request):
    technicians = MaintenanceTechnician.objects.all()
    return render(request, 'technician_list.html', {'technicians': technicians})



def technician_list(request):
    query = request.GET.get('q')
    if query:
        technicians = MaintenanceTechnician.objects.filter(specialization__icontains=query)
    else:
        technicians = MaintenanceTechnician.objects.all()
    return render(request, 'technician_list.html', {'technicians': technicians, 'query': query})



def registration_success(request):
    return render(request, 'registration_success.html')
