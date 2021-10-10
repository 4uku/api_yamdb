from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == 'admin'


class AdminOrUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.role == 'moderator'


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user.is_superuser or request.user.role == 'admin'


class ReviewPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.method == 'POST' and request.user.is_authenticated:
            return True
        return (request.user == obj.author
                or request.user.role == ('admin' or 'moderator'))
