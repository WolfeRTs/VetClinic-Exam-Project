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

    #TODO: Set up vet permissions
    vet_permissions = ['add_medicalreport', 'change_medicalreport', 'delete_medicalreport']
    permissions = Permission.objects.filter(codename__in=vet_permissions)

    if instance.is_vet:
        instance.groups.add(vet_group)
        instance.user_permissions.add(*permissions)

    else:
        instance.groups.remove(vet_group)
        instance.user_permissions.remove(*permissions)


#TODO: Add a signal that populates all med records with the name of the deleted doctor pre_delete