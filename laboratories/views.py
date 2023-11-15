from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from .models import Test, TestResultsPdf, Lab
from .forms import LabCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin



class CreateLaboratory(LoginRequiredMixin, CreateView):

	model = Lab
	template_name = 'laboratories/create_lab.html'
	success_url = '/'

	fields = ['lab_name', 'logo', 'acreditation_code', 'digital_address', 'region_of_location', 
	'telephone', 'email_address', 'website']



class UpdateLaboratory(LoginRequiredMixin, UpdateView):

	model = Lab
	template_name = 'laboratories/update_lab.html'
	success_url = '/'

	fields = ['lab_name', 'logo', 'acreditation_code', 'digital_address', 'region_of_location', 
	'telephone', 'email_address', 'website']



class CreateTest(LoginRequiredMixin, CreateView):

	model = Test
	template_name = 'laboratories/create_test.html'
	success_url = '/'
	fields = ['laboratory', 'department', 'test_name', 'price', 'discount', 'apply_discount']



class UpdateTest(LoginRequiredMixin, UpdateView):

	model = Test
	template_name = 'laboratories/create_test.html'
	success_url = '/'
	fields = ['laboratory', 'department', 'test_name', 'price', 'discount', 'apply_discount']



class DeleteTest(LoginRequiredMixin, DeleteView):

	model = Test

	success_url = '/'

	def get_queryset(self):
		queryset = super().get_queryset()

		return queryset.filter(created_by=self.request.user)



class AddResults(LoginRequiredMixin ,CreateView):

	model = TestResultsPdf
	success_url = '/'
	template_name = 'laboratories/create_test.html'
	fields = ['laboratory', 'hospital', 'test', 'upload_pdf']



class EditTestResults(LoginRequiredMixin, UpdateView):
	model = TestResultsPdf
	success_url = '/'
	template_name = 'laboratories/create_test.html'
	fields = ['laboratory', 'hospital', 'test', 'upload_pdf']



class ResultsDetail(DetailView):

	model = TestResultsPdf

	slug_url_kwarg = 'pk'

	context_object_name = 'results'

	template_name = 'laboratories/test_detail.html'