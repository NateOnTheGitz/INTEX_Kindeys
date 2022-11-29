from django.shortcuts import render
from .models import Food_Log
 
# Create your views here.
def indexPageView(request):
    context = {
 
    }
    return render(request, 'landing_page.html', context)


def createAccountPageView(request) :
    context = {
 
    }
    return render(request, 'create_account.html', context) 


def foodEntryPageView(request) :
    data = Food_Log.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'food_entry.html', context) 

def reportsPageView(request) :
    context = {
 
    }
    return render(request, 'reports.html', context) 