from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.indexPageView, name='dashboard-index'),
    path('account/', views.createAccountPageView, name='create_account'),
    path('foodentry/', views.foodEntryPageView, name='food_entry'),
    path('reports/', views.reportsPageView, name='reports'),
    path('login/', views.loginPageView, name='login'),
    path('add/', views.loginPageView, name='add_food'),
]
