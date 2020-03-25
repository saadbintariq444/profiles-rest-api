from rest_framework import permissions
class UpdateOwnProfile(permissions.BasePermission):
    """ allow to update only your own profile """

    def has_object_permission(self, request,  view , obj):
            """ check user is making change to their  own profile """
            if request.method in permissions.SAFE_METHODS:
                return True
            return obj.id==request.user.id
