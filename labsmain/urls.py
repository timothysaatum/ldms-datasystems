from django.urls import path
from .views import HomeView


APP_NAME = 'labsmain'
urlpatterns = [
    path('', HomeView.as_view(), name='index')
]