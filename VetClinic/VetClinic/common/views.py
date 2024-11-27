from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import TemplateView

from VetClinic.accounts.models import Profile, CustomUser
from VetClinic.images.models import Image
from VetClinic.pets.models import Pet
from VetClinic.services.models import Service, Medicine


class HomePageView(TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['carousel_images'] = Image.objects.filter(category='Carousel').order_by('?')[:5]
        context['minigallery_images'] = Image.objects.filter(category='Gallery').order_by('-date_uploaded')[:7]
        return context


class VetDashboardView(TemplateView):
    template_name = 'common/vet-dashboard.html'


def search_view(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', 'all')

    pets, profiles, services, medicines = [], [], [], []

    if category == 'all' or category == 'pets':
        pets = Pet.objects.filter(
            Q(name__icontains=query)
        ).values('id', 'name', 'owner__profile__first_name', 'owner__profile__last_name', 'owner__username')

    if category == 'all' or category == 'profiles':
        profiles = CustomUser.objects.filter(
            Q(username__icontains=query) | Q(profile__first_name__icontains=query) | Q(profile__last_name__icontains=query) | Q(email__icontains=query)
        ).values('id', 'profile__first_name', 'profile__last_name', 'username', 'email')

    if category == 'all' or category == 'services':
        services = Service.objects.filter(
            Q(name__icontains=query)
        ).values('id', 'name', 'description')

    if category == 'all' or category == 'medicines':
        medicines = Medicine.objects.filter(
            Q(name__icontains=query)
        ).values('id', 'name', 'description', 'dosages')

    return JsonResponse({
        'pets': list(pets),
        'profiles': list(profiles),
        'services': list(services),
        'medicines': list(medicines),
    })
