from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import JsonResponse, HttpResponseForbidden
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

from VetClinic.accounts.models import CustomUser
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


class VetDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'common/vet-dashboard.html'

    def test_func(self):
        return self.request.user.groups.filter(name='Veterinarian').exists() or self.request.user.is_staff


class ContactsView(TemplateView):
    template_name = 'common/contacts.html'


class AboutUsView(TemplateView):
    template_name = 'common/about-us.html'


class DoctorsView(TemplateView):
    template_name = 'common/doctors.html'


@login_required
def search_view(request):
    if (not request.user.is_authenticated
        or not (request.user.is_staff or request.user.groups.filter(name='Veterinarian').exists())
    ):
        return HttpResponseForbidden(_("You do not have permission to access this view."))

    query = request.GET.get('q', '')
    category = request.GET.get('category', 'all')

    pets, profiles, services, medicines = [], [], [], []

    if category == 'all' or category == 'pets':
        pets = Pet.objects.filter(
            Q(name__icontains=query)
        ).values('id', 'name', 'owner__profile__first_name', 'owner__profile__last_name', 'owner__username')

    if category == 'all' or category == 'profiles':
        profiles = CustomUser.objects.filter(
            Q(profile__first_name__icontains=query) | Q(profile__last_name__icontains=query) | Q(username__icontains=query) | Q(email__icontains=query)
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
