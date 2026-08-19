from django.http import HttpResponse
from django.shortcuts import render


def base(Request):
   # return HttpResponse("<p> Hello world</p>")
   return render(request=Request, template_name='base.html')

def connexion (Request):
   return render(request=Request, template_name='connexion.html')