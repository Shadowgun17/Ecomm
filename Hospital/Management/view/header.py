from django.shortcuts import render

# Create your views here.
def Header(request):
    return render(request,'header.html')