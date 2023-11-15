from django import forms
from .models import Hospital


#form for the adding of a hospital
class SampleCreationForm(forms.ModelForm):

	class Meta:

		model = Hospital

		exclude = ('generated_on',)
