from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_superuser)


class IsStaffAuthenticated(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user
                    and request.user.is_authenticated
                    and request.user.is_staff)
