from django.shortcuts import render, redirect
from .forms import Food_Log_Form, Add_Food, NewUserForm, Person_info
from .models import Food_Log, Recommended_Levels, Food_Ingredient, Person, Food_Ingredient, Measurement
from datetime import datetime, timedelta
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


loggedIn=get_user_model()

# Create your views here.
def indexPageView(request):
    context = {
        
    }

    return render(request, 'landing_page.html', context)


def createAccountPageView(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect('person_info')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="create_account.html", context={"register_form":form})

def personinfoPageView(request):
    # form = Person_info()
    if request.method == 'POST':
        form = Person_info(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-index') 
    else:
        form = Person_info()
    context = {
        'form': form,
    }
    return render(request, 'person_info.html', context)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard-index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def foodEntryPageView(request) :
    data = Food_Log.objects.all()
    if request.method == 'POST':
        form = Food_Log_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_entry')  # 'foodentry/'
    else:
        form = Food_Log_Form()
    users = Person.objects.all()    
    
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
    users = Person.objects.all()    
    
    context = {
        'data': data,
        'form': form,
        'users': users,
    }
    return render(request, 'add_food.html', context) 

def reportsPageView(request) :
    test = request.user.username
    curr_username = "TheRealMG"
    nutrientType = "protien"
    timeRange = 7
    curr_date = datetime.today().date()
    if request.method == 'POST':
        nutrientType = request.POST["nutrientSelect"]
        curr_date = datetime.strptime(request.POST["startDate"],'%Y-%m-%d').date()
        timeRange = int(request.POST["dateRange"])
    else: 
        nutrientType = ""
        timeRange = 7
        curr_date = datetime.today().date()

    # DATA FOR BAR GRAPH 
    curr_user_object = Person.objects.filter(username=curr_username).values() 
    curr_date_for_bar = datetime.today().date()

    if len(curr_user_object) > 0:
        for row in curr_user_object:
            curr_user = {
            "first_name": row['first_name'],
            "last_name": row['last_name'],
            "gender": row['gender'],
            "username": row['username'],
            "password": row['password'],
            "email": row['email'],
            "stage": row['stage'],
            "comorbidity": row['comorbidity'],
            "date_of_birth": row['date_of_birth'],
            "weight_lbs": row['weight_lbs'],
            "height_in": row['height_in'],
            }
        userFound = True
    else: 
        #SHOULD BE ERROR
        userFound = False
        curr_user = 0 

    logs_by_day = Food_Log.objects.filter(date=curr_date_for_bar).filter(username__username=curr_username).values()
    sodiumByDay = 0
    potassiumByDay = 0
    waterByDay = 0
    phosByDay = 0
    protienByDay = 0
    if len(logs_by_day) > 0:
        for counter in range(0, len(logs_by_day)):
            sodium = 0
            potassium = 0
            water = 0
            phos = 0
            protien= 0
            quantity = logs_by_day[counter]['quantity']
            food_log_id = logs_by_day[counter]['id']
            micro_values_for_log = Food_Ingredient.objects.filter(food_log__id=food_log_id).values()
            sodium = micro_values_for_log[0]["sodium_mg"] * quantity
            potassium = micro_values_for_log[0]["potassium_mg"] * quantity
            water = micro_values_for_log[0]["water_L"] * quantity
            phos = micro_values_for_log[0]["phos_mg"] * quantity
            protien= micro_values_for_log[0]["protien_g"] * quantity
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
        "protien": protienByDay,
        }
        logsFound = True
    else: 
        #SHOULD BE ERROR
        actualByDay = 0
        logsFound = False

     # DATA FOR BAR GRAPH LIMITS    
    recMicroNutrients = Recommended_Levels.objects.values()
    for row in recMicroNutrients:
        recByMicro = {
        "sodium_min": row['rec_sodium_mg_min'],
        "sodium_max": row['rec_sodium_mg_max'],
        "potassium_min": row['rec_potassium_mg_min'],
        "potassium_max": row['rec_potassium_mg_max'],
        "phos_min": row['rec_phos_mg_min'],
        "phos_max": row['rec_phos_mg_max'],
        "water_m": row["rec_water_L_male"],
        "water_f": row["rec_water_L_female"],
        "protien_limit": row["rec_protein_g_by_kg"] * curr_user['weight_lbs'],
        "test": test,
        }

    #BAR GRAPH CHECK DATA EXCEEDS LIMITS
    #Water
    if curr_user["gender"] == "M" or "m" or "Male" or "male":
        if actualByDay['water'] > 3.7 :
            waterAlert = True
    else :
        if actualByDay['water'] > 2.7 :
            waterAlert = True

    if actualByDay['sodium'] > recByMicro['sodium_max'] :
        sodiumAlert = True
    else :
        sodiumAlert = False

    if actualByDay['potassium'] > recByMicro['potassium_max'] :
        potassiumAlert = True
    else :
        potassiumAlert = False

    if actualByDay['phos'] > recByMicro['phos_max'] :
        phosAlert = True
    else :
        phosAlert = False

    if actualByDay['protien'] > recByMicro['protien_limit'] :
        protienAlert = True
    else :
        protienAlert = False
    # DATA FOR LINE GRAPH
    datesWeek = [] # gets the dates for the last week
    for i in range(0, timeRange):
        datesWeek.append(curr_date + timedelta(days=i))
    
    sliceNutrient = []
    for counter in range(0,timeRange):
        nutrientConsumed = 0
        increment_date = datesWeek[counter]
        logs_by_day = Food_Log.objects.filter(date=increment_date).filter(username__username=curr_username).values()
        for log in logs_by_day:
            quantity = log['quantity']
            food_log_id = log['id']
            micro_values_for_log = Food_Ingredient.objects.filter(food_log__id=food_log_id).values()
            # can call index 0 bc this matches on a pk  and will always return just one record but it's wrapped in a slice
            if nutrientType == "sodium": 
                nutrient = micro_values_for_log[0]["sodium_mg"] * quantity 
            elif nutrientType ==  "potassium":
                nutrient = micro_values_for_log[0]["potassium_mg"] * quantity
            elif nutrientType == "water":
                nutrient = micro_values_for_log[0]["water_L"] * quantity
            elif nutrientType == "phos":
                nutrient = micro_values_for_log[0]["phos_mg"] * quantity
            else: 
                nutrient = micro_values_for_log[0]["protien_g"] * quantity
            nutrientConsumed += nutrient
        sliceNutrient.append(nutrientConsumed)

    # CONTEXT DICTIONARY 
    context = {
        "recByMicro": recByMicro,
        "datesWeek": datesWeek,
        "curr_date": curr_date,
        "sliceNutrient": sliceNutrient,
        "nutrientType": nutrientType,
        'curr_user': curr_user,
        'actualByDay': actualByDay,
        'timeRange': timeRange,
        'logsFound': logsFound,
        'userFound': userFound,
        'waterAlert': waterAlert,
        'sodiumAlert': sodiumAlert,
        'potassiumAlert' : potassiumAlert,
        'phosAlert' : phosAlert,
        'protienAlert' : protienAlert,

        # 'test': test,
    }
    return render(request, 'reports.html', context) 


def editPageView(request) :
    data = Food_Log.objects.all()
    context = {
        'data': data,
    }
    return render(request, 'edit.html', context) 

    
def delete(request, id) :
    log = Food_Log.objects.get(id=id)
    log.delete()
    return redirect ('editpage')

def edit(request, id):
    mylog = Food_Log.objects.get(id=id)
    foods = Food_Ingredient.objects.all()
    measures = Measurement.objects.all()
    if request.method == 'POST':
        new_date = request.POST['date']
        new_meal_type = request.POST['meal_type']
        new_food_name = request.POST['food_name']
        new_quantity = request.POST['quantity']
        new_measurement = request.POST['measurement']
        mylog.date = new_date
        mylog.meal_type = new_meal_type
        mylog.food_name = Food_Ingredient.objects.get(id = id)
        mylog.quantity = new_quantity
        mylog.measurement = Measurement.objects.get(id = id)
        mylog.save()
    context={
        'record': mylog,
        'foods': foods,
        'measures': measures
    }
    return render(request, 'update.html', context)

def selectPageView(request) :
    users = Person.objects.all()
    if request.method == 'POST':
        return redirect('reports')  
    context = {
        'users': users
    }
    return render(request, 'select_landing.html', context) 

def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("dashboard-index")