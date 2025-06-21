from django.conf import settings
from rest_framework import permissions
class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        if not settings.SECURITY_ENABLED:
            return True  # bypass all checks
        return bool(request.user and request.user.is_authenticated)


class PublicReadOnly(permissions.BasePermission):
    """
    Custom permission to allow unrestricted GET requests.
    """
    def has_permission(self, request, view):
        if not settings.SECURITY_ENABLED:
            return True  # bypass all checks

        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return request.user and request.user.is_authenticated
