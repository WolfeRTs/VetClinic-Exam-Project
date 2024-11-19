from django.db.models.signals import post_save
from django.dispatch import receiver

from VetClinic.pets.models import Pet, PetStatus


@receiver(post_save, sender=Pet)
def create_pet_status(sender, instance, created, **kwargs):
    if created:
        PetStatus.objects.create(pet=instance)
