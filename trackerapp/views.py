from django.shortcuts import render, redirect
from .forms import Food_Log_Form
from .forms import Add_Food
from .forms import Create_User
from .models import Food_Log, Recommended_Levels, Food_Ingredient, Measurement, User, Food_Ingredient
from datetime import date
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
    recMicroNutrients = Recommended_Levels.objects.values( "rec_sodium_mg_min", 
    "rec_sodium_mg_max", 
    "rec_potassium_mg_min",
    "rec_potassium_mg_max",
    "rec_phos_mg_min",
    "rec_phos_mg_max",
    "rec_water_L_male",
    "rec_water_L_female",
    "rec_protein_g_by_kg") # excludes "stage" field

    datesWeek = [] # gets the dates for the last week
    today = date.today()
    for i in range(0,7):
        datesWeek.append(today - timedelta(days=i))

    actualSodiumValue = Food_Ingredient.objects.filter(food_log__date='2022-11-28').values_list("sodium_mg", "id", named=True)

    test =  actualSodiumValue[0]
    
    test = Food_Log.objects.filter(date="2022-11-28").values_list("quantity", 'id', named=True)
    
    # actualSodiumValue = Food_Ingredient.objects.filter(food_log__id=cur_id).values_list("sodium_mg", "id", named=True)
    # for pair in actualSodiumValue:
    #     start = pair.find("id")
    #     rowID = pair[start:]
    # actualSodiumValue = Food_Log.objects.filter(id='2022-11-28').values_list("sodium_mg","id", named=True)

    context = {
        "recMicroNutrients": recMicroNutrients,
        "datesWeek": datesWeek,
        "today": today,
        "actualSodiumValue": actualSodiumValue,
        # "actualSodiumQuantity": actualSodiumQuantity,
        "test": test,

    }
    return render(request, 'reports.html', context) 