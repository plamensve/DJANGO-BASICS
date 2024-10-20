from django.shortcuts import render

def home_no_profile(request):
    return render(request, 'home-no-profile.html')

def home_with_profile(request):
    return render(request, 'home-with-profile.html')