from rest_framework.permissions import IsAdminUser, BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(IsAdminUser):
    def has_permission(self, request, view):
        # Allow read-only permissions for all requests
        if request.method in SAFE_METHODS:
            return True
        else:
            admin_permission = bool(request.user and request.user.is_staff)
            return admin_permission


class IsReviewAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read-only permissions for all requests
        if request.method in SAFE_METHODS:
            return True
        else:
            # Check if the request user is the author of the review or an admin user
            author_permission = obj.author == request.user or request.user.is_staff
            return author_permission
