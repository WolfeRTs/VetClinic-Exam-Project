import datetime

from django.contrib.auth.models import Group, AnonymousUser
from django.test import TestCase, RequestFactory
from rest_framework.utils import json

from VetClinic.accounts.models import CustomUser
from VetClinic.common.views import search_view
from VetClinic.pets.models import Pet
from VetClinic.services.models import Service, Medicine


class SearchViewTest(TestCase):

    def setUp(self):
        self.vet_group = Group.objects.create(name='Veterinarian')

        self.staff_user = CustomUser.objects.create_user(username='staffuser', email='staffuser@example.com', is_staff=True)
        self.vet_user = CustomUser.objects.create_user(username='vetuser', email='vetuser@example.com')
        self.regular_user = CustomUser.objects.create_user(username='regularuser', email='regularuser@example.com')
        self.vet_user.groups.add(self.vet_group)

        self.pet1 = Pet.objects.create(name='Fluffy', owner=self.staff_user, date_of_birth=datetime.date(2020, 12, 31))
        self.pet2 = Pet.objects.create(name='Bella', owner=self.vet_user, date_of_birth=datetime.date(2020, 12, 31))
        self.service1 = Service.objects.create(name='Grooming', description='Pet grooming service')
        self.service2 = Service.objects.create(name='Vaccination', description='Pet vaccination service')
        self.medicine1 = Medicine.objects.create(name='Anti-flea', description='Flea treatment', dosages='5ml, 10ml')

    def test_unauthenticated_user_access(self):
        request = RequestFactory().get('/search/', {'q': 'test'})
        request.user = AnonymousUser()
        response = search_view(request)
        self.assertEqual(response.status_code, 302)

    def test_regular_user_access(self):
        request = RequestFactory().get('/search/', {'q': 'test'})
        request.user = self.regular_user
        response = search_view(request)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.content, b"You do not have permission to access this view.")

    def test_staff_user_access(self):
        request = RequestFactory().get('/search/', {'q': 'Fluffy', 'category': 'pets'})
        request.user = self.staff_user
        response = search_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['pets']), 1)
        self.assertEqual(data['pets'][0]['name'], 'Fluffy')

    def test_vet_user_access(self):
        request = RequestFactory().get('/search/', {'q': 'Bella', 'category': 'pets'})
        request.user = self.vet_user
        response = search_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['pets']), 1)
        self.assertEqual(data['pets'][0]['name'], 'Bella')

    def test_search_profiles(self):
        request = RequestFactory().get('/search/', {'q': 'staff', 'category': 'profiles'})
        request.user = self.staff_user
        response = search_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['profiles']), 1)
        self.assertEqual(data['profiles'][0]['username'], 'staffuser')

    def test_search_services(self):
        request = RequestFactory().get('/search/', {'q': 'Grooming', 'category': 'services'})
        request.user = self.staff_user
        response = search_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['services']), 1)
        self.assertEqual(data['services'][0]['name'], 'Grooming')

    def test_search_medicines(self):
        request = RequestFactory().get('/search/', {'q': 'Anti-flea', 'category': 'medicines'})
        request.user = self.staff_user
        response = search_view(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEqual(len(data['medicines']), 1)
        self.assertEqual(data['medicines'][0]['name'], 'Anti-flea')
