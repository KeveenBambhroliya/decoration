from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login
from django.core.mail import EmailMessage, send_mail
from django.core.exceptions import ValidationError
# from django.core.validators import validate_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from account.models import User_Profile,ContactForm







# Create your views here.



# only for test


def test(request):
    return render(request,'test.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.error(request, "username or password is incorrect!!!")
    return render(request,'Frontend/account/Login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')
    

def registration(request):
    if request.method == "POST":   
       
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # Validate password
        if not (
            any(char.isdigit() for char in password1) and
            any(char.islower() for char in password1) and
            any(char.isupper() for char in password1) and
            any(char in "!@#$%^&*()_+{}|;:,.<>?/~`" for char in password1) and
            len(password1) >= 8
        ):
            messages.error(request, "Password must contain at least one number, one uppercase letter, one lowercase letter, one special character, and be at least 8 characters long.")
            return redirect('registration')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username."  )
            return redirect('registration')
        # Validate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('registration')
        # Validate Password
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('registration')
        else:
        # Create user
            my_user = User.objects.create_user(username,email,password1)
            my_user.save()
            return redirect('login')
    return render(request,'Frontend/account/Registration.html')

@login_required(login_url='login')
def user_profile(request):
    user = request.user
    user_profile = User_Profile.objects.get(user=user)

    context = {
        'user_data': user,
        'profile_data': user_profile,
    }

    return render(request,'Frontend/account/user_profile.html',context)


@login_required(login_url='login')
def edit_user_profile(request):
    user = request.user
    user_profile, create = User_Profile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.save()

        user_profile.mobile_number = request.POST.get('mobile_number')
        user_profile.gender = request.POST.get('gender')
        user_profile.birthdate = request.POST.get('birthdate')
        user_profile.save()

        # messages.success(request, 'Profile updated successfully.')
        return redirect('/')
    return render(request,'Frontend/account/edit_user_profile.html', {'user': user, 'user_profile': user_profile})


@login_required(login_url='login')
def user_contactus(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        user = request.user
        user_profile = User_Profile.objects.get(user=user)
        user_profile_id = user_profile.id
        ContactForm.objects.create( user_profile_id=user_profile_id,email=email,fullname=fullname, subject=subject, message=message)
        return redirect('/') 
    return render(request,'Frontend/account/contactus.html')


def user_aboutus(request):
    return render(request,'Frontend/account/aboutus.html')