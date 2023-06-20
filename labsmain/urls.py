from django.urls import path
from .views import home


APP_NAME = 'labsmain'
urlpatterns = [
    path('', home, name='index')
]