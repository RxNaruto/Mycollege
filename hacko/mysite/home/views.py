
# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Signup

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        # Handle form submission
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        name = request.POST['name']

        # Create a new user instance
        user = Signup.objects.create_user(username=username, email=email, password=password, name=name)

        # Flash a success message
        messages.success(request, 'Signup successful!')

        # Redirect to a success page or login page
        return redirect('/')  # Replace 'success' with the appropriate URL name
    else:
        # Render the signup form
        return render(request, 'signup.html')
    
def explore(request):
    return render(request,'explore.html')

def projectsfn(request):
    return render(request, 'projectsfn.html')

