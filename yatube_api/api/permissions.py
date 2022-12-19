from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if bool(request.user and request.user.is_authenticated):
            return obj.author == request.user
        return False
