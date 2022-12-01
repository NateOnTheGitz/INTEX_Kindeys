from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.indexPageView, name='dashboard-index'),
    path('account/', views.createAccountPageView, name='create_account'),
    path('foodentry/', views.foodEntryPageView, name='food_entry'),
    path('reports/', views.reportsPageView, name='reports'),
    path('login/', views.login_request, name='login'),
    path('add/', views.addfoodEntryPageView, name='add_food'),
    path('editpage/', views.editPageView, name='editpage'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),
    # path('update/', views.updatePageView, name='update'),
    # path('select/', views.selectPageView, name='select'),
    path('reports/<str>', views.reportsPageView, name="reports"),
    path('person/', views.personinfoPageView, name='person_info'),
    path("logout", views.logout_request, name= "logout"),


]
 