from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Hospital, Sample
from .forms import SampleCreationForm



class CreateHospital(LoginRequiredMixin, CreateView):
	model = Hospital
	template_name = 'hospitals/hospital.html'
	success_url = '/'
	fields = ['hospital_name', 'digital_address', 'region_of_location', 'telephone', 'email_address', 'website']



class UpdateHospital(LoginRequiredMixin, UpdateView):
	model = Hospital
	success_url = '/'
	template_name = 'hospitals/hospital_update.html'
	fields = ['hospital_name', 'digital_address', 'region_of_location', 'telephone', 'email_address', 'website']

	def get_queryset(self):

		queryset = super().get_queryset()

		return queryset.filter(created_by=self.request.user)



class CreateSample(LoginRequiredMixin, CreateView):

	model = Sample
	template_name = 'hospitals/datacollection.html'
	success_url = '/'
	fields = ['hospital', 'send_to', 'send_by', 'sample_container_type', 'sample_id', 'sample_image', 'sample_origin',
	 'sex_of_client', 'name_of_client', 'age_of_client', 'department', 'test_to_be_done', 'is_delivered']



class UpdateSample(LoginRequiredMixin, UpdateView):
	model = Sample
	success_url = '/'
	template_name = 'hospitals/sample_update.html'
	fields = ['hospital', 'send_to', 'send_by', 'sample_container_type', 'sample_id', 'sample_image', 'sample_origin',
	 'sex_of_client', 'name_of_client', 'age_of_client', 'department', 'test_to_be_done', 'is_delivered']



class DeleteSample(LoginRequiredMixin, DeleteView):
	model = Sample

	success_url = '/'

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(hospital__created_by=self.request.user)
