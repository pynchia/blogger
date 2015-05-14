from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only admins to add/edit an object
    """

    def has_permission(self, request, view):  # when creating obj
        # always allow GET, HEAD and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff


    def has_object_permission(self, request, view, obj):  # when editing obj
        return self.has_permission(request, view)


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the author to edit an article
    """

    def has_object_permission(self, request, view, obj):
        # always allow GET, HEAD and OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

