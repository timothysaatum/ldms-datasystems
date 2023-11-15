from django.urls import path
from .views import (CreateLaboratory, UpdateLaboratory, CreateTest, UpdateTest, 
	DeleteTest, AddResults, EditTestResults, ResultsDetail)


urlpatterns = [

	path('create/', CreateLaboratory.as_view(), name='create-lab'),
	path('update/<int:pk>/lab/', UpdateLaboratory.as_view(), name='update-lab'),
	path('create/test/', CreateTest.as_view(), name='create-test'),
	path('update/<int:pk>/test/', UpdateTest.as_view(), name='update-test'),
	path('delete/<int:pk>/test/', DeleteTest.as_view(), name='delete-test'),
	path('add/results/', AddResults.as_view(), name='add-results'),
	path('edit/test/<int:pk>/results/', EditTestResults.as_view(), name='edit-test'),
	path('results/details/<int:pk>/', ResultsDetail.as_view(), name='result-detail')

]
