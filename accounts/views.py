from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from PIL import Image

import logging

logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'accounts/home.html')

def picture_edit(request):
    if request.method =='POST':
        text = request.POST.get("cv")
        width = int(request.POST.get("width"))
        height = int(request.POST.get("height"))
        img = Image.open(text)
        img = img.resize((width, height), Image.ANTIALIAS)
        logger.info("Image file: " + text+" has been edited to size " + str(width) + " x " + str(height))
        img.save(text)
        img.show()
        return render(request, 'accounts/picture_edit.html')
    else:
        return render(request, 'accounts/picture_edit.html')

def sign_in(request):
    if request.method =='POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info("Username: " + username + " Login successful")
            return HttpResponseRedirect('/account/picture_edit/')
        # Redirect to a success page.
        else:
            logger.warning("Login Failed: Invalid Username or Password")
            return HttpResponseRedirect('/account/login/')
    else:
        return render(request, 'accounts/login.html')



def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.cleaned_data.get('username')
            logger.info("A new account has been created. ID: " + user)
            form.save()
            return HttpResponseRedirect('/account')
        else:
            print(form.errors)
            return render(request, 'accounts/reg_form.html', args)
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)
# Create your views here.
