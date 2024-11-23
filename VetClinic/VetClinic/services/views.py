from django.views.generic import ListView
from rest_framework.decorators import api_view

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
        return ServiceCategory.objects.all()


class ServicesByCategoryAPIView(APIView):
    def get(self, request, category_id):
        category = get_object_or_404(ServiceCategory, pk=category_id)

        services = Service.objects.filter(category=category.pk).order_by('name')

        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)
