from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def organization_portal(request):
    return render(request, 'organization.html')

def submit_info(request):
    return render(request, 'submitinfo.html')

