from django import forms
from .models import Lab, Test


class LabCreationForm(forms.ModelForm):
	
	 test_scope = forms.ModelMultipleChoiceField(queryset=Test.objects.all(), 
		widget=forms.CheckboxSelectMultiple, required=True)

	 class Meta:
	 	model = Lab
	 	fields = ['lab_name', 'digital_address', 'region_of_location', 'telephone', 'email_address', 'website']