from django.shortcuts import render, redirect
from .forms import Food_Log_Form
from .forms import Add_Food
from .forms import Create_User
from .models import Food_Log, Recommended_Levels, Food_Ingredient, Measurement, User, Food_Ingredient
from datetime import datetime
from datetime import timedelta

# Create your views here.
def indexPageView(request):
    context = {
 
    }
    return render(request, 'landing_page.html', context)


def createAccountPageView(request) :
    data = User.objects.all()
    if request.method == 'POST':
        form = Create_User(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Create_User()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'create_account.html', context) 

def loginPageView(request):
    context = {

    }
    return render(request, 'login.html', context)


def foodEntryPageView(request) :
    data = Food_Log.objects.all()
    if request.method == 'POST':
        form = Food_Log_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_entry')  # 'foodentry/'
    else:
        form = Food_Log_Form()
    users = User.objects.all()    
    
    context = {
        'data': data,
        'form': form,
        'users': users,
    }
    return render(request, 'food_entry.html', context) 

def addfoodEntryPageView(request) :
    data = Food_Ingredient.objects.all()
    if request.method == 'POST':
        form = Add_Food(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_food')  # 'foodentry/'
    else:
        form = Add_Food()
    users = User.objects.all()    
    
    context = {
        'data': data,
        'form': form,
        'users': users,
    }
    return render(request, 'add_food.html', context) 

def reportsPageView(request) :
    users = User.objects.all()
    recMicroNutrients = Recommended_Levels.objects.values() # excludes "stage" field
    for row in recMicroNutrients:
        recByMicro = { #dictionary for min/max on bar graphs for each micro 
        "sodium_min": row['rec_sodium_mg_min'],
        "sodium_max": row['rec_sodium_mg_max'],
        "potassium_min": row['rec_potassium_mg_min'],
        "potassium_max": row['rec_potassium_mg_max'],
        "phos_min": row['rec_phos_mg_min'],
        "phos_max": row['rec_phos_mg_max'],
        "water_m": row["rec_water_L_male"],
        "water_f": row["rec_water_L_female"],
        "protien_ratio": row["rec_protein_g_by_kg"],
        }

    curr_date = datetime.strptime("11-27-2022", '%m-%d-%Y').date()  #needs to be passed in by a parameter to this function 
    
    curr_user = "TheRealMG" #needs to be passed in by a parameter to this function 
    logs_by_day = Food_Log.objects.filter(date=curr_date).filter(username__username=curr_user).values()
    for counter in range(0, len(logs_by_day)-1):
        sodiumByDay = 0
        potassiumByDay = 0
        waterByDay = 0
        phosByDay = 0
        protienByDay = 0
        quantity = logs_by_day[counter]['quantity']
        food_log_id = logs_by_day[counter]['id']
        micro_values_for_log = Food_Ingredient.objects.filter(food_log__id=food_log_id).values()
        sodium = micro_values_for_log[counter]["sodium_mg"] * quantity
        potassium = micro_values_for_log[counter]["potassium_mg"] * quantity
        water = micro_values_for_log[counter]["water_L"] * quantity
        phos = micro_values_for_log[counter]["phos_mg"] * quantity
        protien = micro_values_for_log[counter]["protien_g"] * quantity
        sodiumByDay += sodium
        potassiumByDay += potassium
        waterByDay += water
        phosByDay += phos
        protienByDay += protien
    actualByDay = {
    "sodium": sodiumByDay,
    "potassium": potassiumByDay,
    "water": waterByDay,
    "phos": phosByDay,
    "protien": protienByDay
    }

    datesWeek = [] # gets the dates for the last week
    for i in range(0,7):
        datesWeek.append(curr_date - timedelta(days=i))
    
    sliceSodium = []
    slicePotassium = []
    sliceWater = []
    slicePhos = []
    sliceProtien = []
    for counter in range(0,7):
        sodiumConsumed = 0
        potassiumConsumed = 0
        waterConsumed = 0
        phosConsumed = 0
        protienConsumed = 0
        curr_date = datesWeek[counter]
        logs_by_day = Food_Log.objects.filter(date=curr_date).filter(username__username=curr_user).values()
        for log in logs_by_day:
            quantity = log['quantity']
            food_log_id = log['id']
            micro_values_for_log = Food_Ingredient.objects.filter(food_log__id=food_log_id).values()
            # can call index 0 bc this matches on a pk  and will always return just one record but it's wrapped in a slice
            sodium = micro_values_for_log[0]["sodium_mg"] * quantity 
            potassium = micro_values_for_log[0]["potassium_mg"] * quantity
            water = micro_values_for_log[0]["water_L"] * quantity
            phos = micro_values_for_log[0]["phos_mg"] * quantity
            protien = micro_values_for_log[0]["protien_g"] * quantity
            sodiumConsumed += sodium
            potassiumConsumed += potassium
            waterConsumed += water
            phosConsumed += phos
            protienConsumed += protien
        sliceSodium.append(sodiumConsumed)
        slicePotassium.append(potassiumConsumed)
        sliceWater.append(waterConsumed)
        slicePhos.append(phosConsumed)
        sliceProtien.append(protienConsumed)

    test = sliceSodium

    
    context = {
        "recByMicro": recByMicro,
        "datesWeek": datesWeek,
        "curr_date": curr_date,
        "test": test,
        'users': users,
        'actualByDay': actualByDay

    }
    return render(request, 'reports.html', context) 


def editPageView(request) :
    data = Food_Log.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'edit.html', context) 

    
def delete(request) :
    pass

def edit(request):
    pass