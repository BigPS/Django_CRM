from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User  # Import the User model
from django.contrib.auth import authenticate, login


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # Retrieve user input from the form
        email = request.POST.get('email')
        password = request.POST.get('pass')

        # Check if the email is already in use
        if User.objects.filter(username=email).exists():
            # Handle the case where the email is already registered
            return render(request, 'register.html', {'error_message': 'Email already registered.'})
        else:
            # Create a new user
            user = User.objects.create_user(username=email, password=password)

            # Log in the user after registration
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)

            # Redirect the user to a success page or any other page as needed
            return redirect('home')  # Replace 'home' with the URL name of your home page


# class SigninView(View):
#     def get(self, request):
#         return render(request, 'sign-in.html')

@method_decorator(login_required, name='dispatch')
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


@method_decorator(login_required, name='dispatch')
class ContactsView(View):
    def get(self, request):
        return render(request, 'contacts.html')


@method_decorator(login_required, name='dispatch')
class CompaniesView(View):
    def get(self, request):
        return render(request, 'companies.html')


@method_decorator(login_required, name='dispatch')
class JobsView(View):
    def get(self, request):
        return render(request, 'jobs.html')


@method_decorator(login_required, name='dispatch')
class CandidatesView(View):
    def get(self, request):
        return render(request, 'candidates.html')


@method_decorator(login_required, name='dispatch')
class DealsView(View):
    def get(self, request):
        return render(request, 'deals.html')


@method_decorator(login_required, name='dispatch')
class ChatGPTView(View):
    def get(self, request):
        return render(request, 'chatgpt.html')
