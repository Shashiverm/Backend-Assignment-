from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsAdminUserOrReadOnly(BasePermission):
    """
    Custom permission to only allow admin users to edit an object.
    Non-admin users can only view the object.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff

class IsEligibleForLoan(BasePermission):
    """
    Custom permission to check if a user is eligible for a loan.
    """

    def has_permission(self, request, view):
        # Implement eligibility logic here
        return request.user.is_authenticated and request.user.approved_limit > 0