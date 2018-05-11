from django.contrib.auth.models import User
from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, new_contact, contacts
from .models import Contact
from .forms import NewContactForm

class HomeTests(TestCase):
	def setUp(self):
		User.objects.create_user(username='john', email='john@doe.com', password='123')
	
	def test_home_view_status_code(self):
		url = reverse('home')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_home_url_resolves_home_view(self):
		view = resolve('/')
		self.assertEquals(view.func, home)

	def test_home_view_contains_navigation_links(self):
		homepage_url = reverse('home')
		new_contact_url = reverse('new_contact')

		response = self.client.get(homepage_url)

		self.assertContains(response, 'href="{0}"'.format(new_contact_url))

class ContactTests(TestCase):
	def setUp(self):
		User.objects.create_user(username='john', email='john@doe.com', password='123')
		Contact.objects.create(contact_name='Test', contact_info='testarooni')
		

	def test_contacts_view_success_status_code(self):
		url = reverse('contacts', kwargs={'pk':1})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_contacts_view_not_found_status_code(self):
		url = reverse('contacts', kwargs={'pk':99})
		response = self.client.get(url)
		self.assertEquals(response.status_code, 404)

	def test_contacts_url_resolves_contacts_view(self):
		view = resolve('/contacts/1/')
		self.assertEquals(view.func, contacts)

class NewContactTests(TestCase):
	def setUp(self):
		User.objects.create_user(username='john', email='john@doe.com', password='123')
		

	def test_new_contact_view_success_status_code(self):
		url = reverse('new_contact')
		response = self.client.get(url)
		self.assertEquals(response.status_code, 200)

	def test_new_contact_view_contains_link_back_to_home(self):
		new_contact_url = reverse('new_contact')
		home = reverse('home')
		response = self.client.get(new_contact_url)
		self.assertContains(response, 'href="{0}"'.format(home))

	def test_csrf(self):
		url = reverse('new_contact')
		response = self.client.get(url)
		self.assertContains(response, 'csrfmiddlewaretoken')


	def test_new_contact_valid_data(self):
		url = reverse('new_contact')
		data = {
			'contact_name': 'James',
			'contact_info': 'Person',
		}
		response = self.client.post(url,data)
		self.assertTrue(Contact.objects.exists())

	def test_contains_form(self):
		url = reverse('new_contact')
		response = self.client.get(url)
		form = response.context.get('form')
		self.assertIsInstance(form, NewContactForm)

	def test_new_contact_invalid_post_data(self):
		'''
		invalid post data should not redirect
		expected behavior is to show the form again with validation errors
		'''

		url = reverse('new_contact')
		response = self.client.post(url, {})
		form = response.context.get('form')
		self.assertEquals(response.status_code, 200)
		self.assertTrue(form.errors)



