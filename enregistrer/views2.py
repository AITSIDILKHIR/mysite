from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def enreg(request):
    template=loader.get_template('enregistrer.html')
    return HttpResponse(template.render())

# Create your views here.
