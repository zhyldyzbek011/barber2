from rest_framework.permissions import BasePermission
from rest_framework import permissions


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        print("PERMISSION CLASS WORKED")
        print(request)
        return request.user == obj.owner


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if view.name == 'Add to liked':
            return request.user.is_active
        if view.name == 'Remove from liked':
            return request.user.is_active
        return obj.owner == request.user