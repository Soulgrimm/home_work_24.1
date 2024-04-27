from rest_framework.permissions import BasePermission


class ViewPerm(BasePermission):

    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_authenticated() is not request.user.is_staff
        elif view.action in ['retrieve', 'update', 'list']:
            return request.user == view.get_object().is_author or request.user.is_staff
        elif view.action == 'destroy':
            return request.user == view.get_object().is_author
        else:
            return False


class IsStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='staff').exists():
            return True
        return False


class IsAuthor(BasePermission):

    def has_permission(self, request, view):
        return request.user == view.get_object().is_author
