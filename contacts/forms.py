from django import forms
from .models import Contact

class NewContactForm(forms.ModelForm):
	contact_info = forms.CharField(
		widget=forms.Textarea(
			attrs={'rows': 5, 'placeholder': 'Enter contact info here'}
		), 
		max_length=1000, 
		# help_text='The max length of contact info is 1000 characters.',
	)

	class Meta:
		model = Contact
		fields = ['contact_name', 'contact_info']

