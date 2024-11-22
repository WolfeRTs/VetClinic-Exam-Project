from rest_framework.serializers import ModelSerializer

from VetClinic.services.models import Service, Medicine


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class MedicineSerializer(ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'