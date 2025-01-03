from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # Handle POST requests (login form submission)
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "You have been successfully logged in!")
            return redirect('home')
        else:
            # Provide feedback for login failure
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('home')

    # Handle GET requests (page visits)
    if request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
        

def logout_user(request):
    # Logout the user and display a success message
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html',{})

