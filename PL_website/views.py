from operator import index
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):

    return render(request,"index.html")



def about(request):
    return render(request, 'PL_websit/about.html') 

def course(self):
    
    
    return HttpResponse('<h1>Welcome to my PL Course page</h1>')
