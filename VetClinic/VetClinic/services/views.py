from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import api_view

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse_lazy
from rest_framework.views import APIView

from VetClinic.services.forms import ServiceAddForm, ServiceEditForm, MedicineAddForm, MedicineEditForm, \
    ServiceDeleteForm
from VetClinic.services.models import Service, Medicine, ServiceCategory
from VetClinic.services.serializers import ServiceSerializer, MedicineSerializer


class ServiceListCreateView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]


class ServiceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    # permission_classes = [IsAuthenticated]


class MedicineListCreateView(ListCreateAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    # permission_classes = [IsAuthenticated]


class MedicineDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    # permission_classes = [IsAuthenticated]


class ServiceCategoriesDashboardView(ListView):
    model = ServiceCategory
    template_name = 'services/services-dashboard.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return ServiceCategory.objects.filter(category_services__isnull=False).distinct()


class ServicesByCategoryAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(ServiceCategory, pk=category_id)

        services = Service.objects.filter(category=category.pk).order_by('name')

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceAddForm
    template_name = 'services/service/service-add.html'
    success_url = reverse_lazy('vet-dashboard')


class ServiceEditView(UpdateView):
    model = Service
    form_class = ServiceEditForm
    template_name = 'services/service/service-edit.html'
    success_url = reverse_lazy('vet-dashboard')
    pk_url_kwarg = 'service_id'


class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineAddForm
    template_name = 'services/medicine/medicine-add.html'
    success_url = reverse_lazy('vet-dashboard')


class MedicineEditView(UpdateView):
    model = Medicine
    form_class = MedicineEditForm
    template_name = 'services/medicine/medicine-edit.html'
    success_url = reverse_lazy('vet-dashboard')
    pk_url_kwarg = 'medicine_id'
