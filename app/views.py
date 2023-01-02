from django.shortcuts import render

# Create your views here.
def stfiles(request):
    return render(request,'stfiles.html')