from rest_framework import permissions


class IsVetUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user
                and request.user.is_authenticated
                and request.user.groups.filter(name='Veterinarian').exists()
                )


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff


def is_vet(user):
    return user.groups.filter(name='Veterinarian').exists()
