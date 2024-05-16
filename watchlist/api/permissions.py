from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS


class AdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            admin_permission = bool(request.user and request.user.is_staff)
            return admin_permission


class ReviewAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        else:
            author_permission = obj.author == request.user
            return author_permission
