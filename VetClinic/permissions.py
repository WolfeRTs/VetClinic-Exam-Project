from rest_framework import permissions


class IsVetUserOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.user
                and request.user.is_authenticated
                and (request.user.groups.filter(name='Veterinarian').exists() or request.user.is_staff)
                )


class IsStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_staff


def is_vet(user):
    return user.groups.filter(name='Veterinarian').exists()
