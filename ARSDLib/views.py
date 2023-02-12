from django.shortcuts import render, HttpResponse

# Create your views here.
def Index(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def membership(request):
    return render(request, 'membership.html')