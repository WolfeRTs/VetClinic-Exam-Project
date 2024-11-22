from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from VetClinic.services.models import Service, Medicine
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

