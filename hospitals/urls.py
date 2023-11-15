from .views import (CreateHospital, CreateSample, UpdateHospital, UpdateSample, DeleteSample)
from django.urls import path


urlpatterns = [
	path('hospital/create/', CreateHospital.as_view(), name='create-hospital'),
	path('sample/create/', CreateSample.as_view(), name='create-sample'),
	path('hospital/<int:pk>/update/', UpdateHospital.as_view(), name='update-hospital'),
	path('sample/update/<int:pk>/', UpdateSample.as_view(), name='update-sample'),
	path('sample/delete/<int:pk>/', DeleteSample.as_view(), name='delete-sample')
]