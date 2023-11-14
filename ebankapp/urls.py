from django.urls import path
from . import views
app_name = 'ebankapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('branch/', views.branch, name = "branch"),

    # Add more URLs as needed
]