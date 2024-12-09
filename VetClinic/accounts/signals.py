from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_save
from django.dispatch import receiver

from VetClinic.accounts.models import Profile

UserModel = get_user_model()

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def add_vet_groups(sender, instance, created, **kwargs):
    vet_group = Group.objects.get(name='Veterinarian')

    if instance.is_vet:
        instance.groups.add(vet_group)
    else:
        instance.groups.remove(vet_group)
