from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import NewContactForm
from datetime import date


def home(request):
	
	contacts = Contact.objects.all()
	
	return render(request, 'home.html', {'contacts': contacts})

def contacts(request, pk):
	contact = get_object_or_404(Contact, pk=pk)
	return render(request, 'contacts.html', {'contact': contact})

def new_contact(request):
	user = User.objects.last() # TODO: get currently logged in user

	if request.method == 'POST':
		form = NewContactForm(request.POST)
		if form.is_valid():
			contact = form.save(commit=False)
			print(user)
			contact.user = user
			contact.save()

			return redirect('home') # redirects home after creating a new contact
	else:
		form = NewContactForm()

	return render(request, 'new_contact.html', {'form': form})	

