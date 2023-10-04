from django.shortcuts import render

# Create your views here.

def register(request):
    return render(request, 'register.html')

def signin(request):
    return render(request, 'sign-in.html')
def home(request):
    return render(request, 'home.html')

def contacts(request):
    return render(request, 'contacts.html')

def companies(request):
    return render(request, 'companies.html')

def jobs(request):
    return render(request, 'jobs.html')

def candidates(request):
    return render(request, 'candidates.html')

def deals(request):
    return render(request, 'deals.html')

def chatgpt(request):
    return render(request, 'chatgpt.html')
