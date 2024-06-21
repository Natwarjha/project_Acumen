from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.greet_user, name='greet'),
    path('process_form/', views.process_form, name='process_form'),
    path('fetch_jokes/', views.fetch_jokes, name='fetch_jokes'),
]

