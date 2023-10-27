from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from item.models import Category, Item
from .forms import SignupForm, LoginForm
from django.contrib import messages
from dashboard.models import UserProfile
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Verify reCAPTCHA
            captcha_value = request.POST.get('g-recaptcha-response', '')
            if not captcha_value or not form.fields['captcha'].verify(captcha_value, request.META.get('REMOTE_ADDR')):
                messages.error(request, "Error verifying reCAPTCHA, please try again.")
            else:
                # reCAPTCHA verification successful
                messages.success(request, "Success!")
                
            # Redirect to the user profile section upon successful captcha verification
            return HttpResponseRedirect(reverse('UserProfile'))
            
        else:
            messages.error(request, "Form validation error!")
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

    


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            #full_name = form.cleaned_data['full_name']
            #address = form.cleaned_data['address']
            #phone_number = form.cleaned_data['phone_number']

            # Create a UserProfile instance and associate it with the user
            #user_profile = UserProfile(user=user, full_name=full_name, address=address, phone_number=phone_number)
            #user_profile.save()

            # Log the user in
            login(request, user)

            return redirect('/dashboard/products/')  # Redirect to the dashboard or a success page
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "index.html" 